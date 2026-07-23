from typing import Any, Dict

from api.api_client import ApiClient
from api.endpoints import ApiEndpoints


EXPECTED_METHOD_ERROR = (
    "This request method is not supported."
)


def test_post_products_list_is_not_supported(
    api_client: ApiClient,
) -> None:
    """Verify POST is not supported for productsList."""

    response = api_client.post(
        ApiEndpoints.PRODUCTS_LIST
    )

    assert response.status_code in {
        200,
        405,
    }, (
        "Expected HTTP status 200 or 405, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload: Dict[str, Any] = (
        api_client.json_body(response)
    )

    assert payload.get("responseCode") == 405, (
        "Expected responseCode 405, "
        f"but received {payload.get('responseCode')}. "
        f"Payload: {payload}"
    )

    assert payload.get("message") == (
        EXPECTED_METHOD_ERROR
    ), (
        "Unexpected error message. "
        f"Received: {payload.get('message')}"
    )


def test_put_brands_list_is_not_supported(
    api_client: ApiClient,
) -> None:
    """Verify PUT is not supported for brandsList."""

    response = api_client.put(
        ApiEndpoints.BRANDS_LIST
    )

    assert response.status_code in {
        200,
        405,
    }, (
        "Expected HTTP status 200 or 405, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload: Dict[str, Any] = (
        api_client.json_body(response)
    )

    assert payload.get("responseCode") == 405, (
        "Expected responseCode 405, "
        f"but received {payload.get('responseCode')}. "
        f"Payload: {payload}"
    )

    assert payload.get("message") == (
        EXPECTED_METHOD_ERROR
    ), (
        "Unexpected error message. "
        f"Received: {payload.get('message')}"
    )