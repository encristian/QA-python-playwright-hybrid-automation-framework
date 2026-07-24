from typing import Any, Dict

from api.api_client import ApiClient
from api.endpoints import ApiEndpoints
from api.user_payloads import (
    build_account_payload,
    build_credentials,
)


def get_response_code(
    payload: Dict[str, Any],
) -> int:
    """Return responseCode as an integer."""

    return int(payload.get("responseCode", 0))


def assert_api_result(
    payload: Dict[str, Any],
    expected_code: int,
    expected_message: str,
) -> None:
    """Verify the logical response code and message."""

    actual_code = get_response_code(payload)
    actual_message = payload.get("message")

    assert actual_code == expected_code, (
        f"Expected responseCode {expected_code}, "
        f"but received {actual_code}. "
        f"Payload: {payload}"
    )

    assert actual_message == expected_message, (
        f"Expected message '{expected_message}', "
        f"but received '{actual_message}'."
    )


def test_user_account_api_lifecycle(
    api_client: ApiClient,
    generated_user: Dict[str, str],
) -> None:
    """Verify create, login, details and delete operations."""

    account_data = build_account_payload(
        generated_user
    )

    credentials = build_credentials(
        generated_user
    )

    account_created = False
    account_deleted = False

    try:
        # Step 1: Create the user account
        create_response = api_client.post(
            ApiEndpoints.CREATE_ACCOUNT,
            data=account_data,
        )

        assert create_response.status_code in {
            200,
            201,
        }, (
            "Expected HTTP status 200 or 201 "
            "when creating the account, "
            f"but received "
            f"{create_response.status_code}. "
            f"Response: "
            f"{create_response.text[:300]}"
        )

        create_payload = api_client.json_body(
            create_response
        )

        assert_api_result(
            payload=create_payload,
            expected_code=201,
            expected_message="User created!",
        )

        account_created = True

        # Step 2: Verify login with valid credentials
        login_response = api_client.post(
            ApiEndpoints.VERIFY_LOGIN,
            data=credentials,
        )

        assert login_response.status_code == 200, (
            "Expected HTTP status 200 for login, "
            f"but received "
            f"{login_response.status_code}. "
            f"Response: "
            f"{login_response.text[:300]}"
        )

        login_payload = api_client.json_body(
            login_response
        )

        assert_api_result(
            payload=login_payload,
            expected_code=200,
            expected_message="User exists!",
        )

        # Step 3: Get the user details by email
        details_response = api_client.get(
            ApiEndpoints.USER_DETAILS,
            params={
                "email": generated_user["email"],
            },
        )

        assert details_response.status_code == 200, (
            "Expected HTTP status 200 "
            "for user details, "
            f"but received "
            f"{details_response.status_code}. "
            f"Response: "
            f"{details_response.text[:300]}"
        )

        details_payload = api_client.json_body(
            details_response
        )

        assert get_response_code(
            details_payload
        ) == 200, (
            "Expected responseCode 200 "
            "for user details. "
            f"Payload: {details_payload}"
        )

        assert "user" in details_payload, (
            "The response does not contain "
            "the 'user' field. "
            f"Payload: {details_payload}"
        )

        user_details = details_payload["user"]

        assert isinstance(user_details, dict), (
            "Expected the user details "
            "to be a dictionary, "
            f"but received "
            f"{type(user_details).__name__}."
        )

        assert user_details.get("email") == (
            generated_user["email"]
        ), (
            "The returned email is different "
            "from the created user's email. "
            f"Expected: {generated_user['email']}. "
            f"Received: {user_details.get('email')}."
        )

        assert user_details.get("name") == (
            generated_user["name"]
        ), (
            "The returned name is different "
            "from the created user's name. "
            f"Expected: {generated_user['name']}. "
            f"Received: {user_details.get('name')}."
        )

        # Step 4: Delete the user account
        delete_response = api_client.delete(
            ApiEndpoints.DELETE_ACCOUNT,
            data=credentials,
        )

        assert delete_response.status_code == 200, (
            "Expected HTTP status 200 "
            "when deleting the account, "
            f"but received "
            f"{delete_response.status_code}. "
            f"Response: "
            f"{delete_response.text[:300]}"
        )

        delete_payload = api_client.json_body(
            delete_response
        )

        assert_api_result(
            payload=delete_payload,
            expected_code=200,
            expected_message="Account deleted!",
        )

        account_deleted = True

        # Step 5: Verify the deleted user cannot log in
        deleted_login_response = api_client.post(
            ApiEndpoints.VERIFY_LOGIN,
            data=credentials,
        )

        assert (
            deleted_login_response.status_code
            in {
                200,
                404,
            }
        ), (
            "Expected HTTP status 200 or 404 "
            "after deleting the account, "
            f"but received "
            f"{deleted_login_response.status_code}."
        )

        deleted_login_payload = (
            api_client.json_body(
                deleted_login_response
            )
        )

        assert_api_result(
            payload=deleted_login_payload,
            expected_code=404,
            expected_message="User not found!",
        )

    finally:
        # Cleanup if the test failed after account creation
        # but before normal account deletion.
        if account_created and not account_deleted:
            api_client.delete(
                ApiEndpoints.DELETE_ACCOUNT,
                data=credentials,
            )


def test_verify_login_with_invalid_credentials(
    api_client: ApiClient,
    generated_user: Dict[str, str],
) -> None:
    """Verify login fails for a user that does not exist."""

    response = api_client.post(
        ApiEndpoints.VERIFY_LOGIN,
        data={
            "email": generated_user["email"],
            "password": generated_user["password"],
        },
    )

    assert response.status_code in {
        200,
        404,
    }, (
        "Expected HTTP status 200 or 404, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload = api_client.json_body(response)

    assert_api_result(
        payload=payload,
        expected_code=404,
        expected_message="User not found!",
    )


def test_verify_login_without_email(
    api_client: ApiClient,
    generated_user: Dict[str, str],
) -> None:
    """Verify login validation when email is missing."""

    response = api_client.post(
        ApiEndpoints.VERIFY_LOGIN,
        data={
            "password": generated_user["password"],
        },
    )

    assert response.status_code in {
        200,
        400,
    }, (
        "Expected HTTP status 200 or 400, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload = api_client.json_body(response)

    assert_api_result(
        payload=payload,
        expected_code=400,
        expected_message=(
            "Bad request, email or password "
            "parameter is missing in POST request."
        ),
    )


def test_delete_verify_login_is_not_supported(
    api_client: ApiClient,
) -> None:
    """Verify DELETE is not supported for verifyLogin."""

    response = api_client.delete(
        ApiEndpoints.VERIFY_LOGIN
    )

    assert response.status_code in {
        200,
        405,
    }, (
        "Expected HTTP status 200 or 405, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload = api_client.json_body(response)

    assert_api_result(
        payload=payload,
        expected_code=405,
        expected_message=(
            "This request method is not supported."
        ),
    )