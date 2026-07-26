from typing import Dict
from urllib.parse import urlparse

from playwright.sync_api import (
    Page,
    Request,
    Response,
    expect,
)

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.network_recorder import NetworkRecorder


def has_path(
    url: str,
    expected_path: str,
) -> bool:
    """Check whether a URL has the expected path."""

    actual_path = (
        urlparse(url)
        .path
        .rstrip("/")
    )

    normalized_expected_path = (
        expected_path.rstrip("/")
    )

    return (
        actual_path
        == normalized_expected_path
    )


def test_products_page_emits_successful_network_events(
    page: Page,
    products_page: ProductsPage,
) -> None:
    """Verify the main Products request and response."""

    recorder = NetworkRecorder()
    recorder.start(page)

    products_page.open()

    products_requests = [
        request
        for request in recorder.requests
        if (
            has_path(
                request.url,
                "/products",
            )
            and request.is_navigation_request
        )
    ]

    assert products_requests, (
        "No navigation request was recorded "
        "for the Products page. "
        f"Recorded requests: {recorder.requests}"
    )

    products_request = products_requests[-1]

    assert products_request.method == "GET", (
        "Expected the Products page to use GET, "
        f"but received {products_request.method}."
    )

    assert (
        products_request.resource_type
        == "document"
    ), (
        "Expected Products to be loaded as "
        "a document request, "
        f"but received resource type "
        f"'{products_request.resource_type}'."
    )

    products_responses = [
        response
        for response in recorder.responses
        if (
            has_path(
                response.url,
                "/products",
            )
            and response.resource_type
            == "document"
        )
    ]

    assert products_responses, (
        "No document response was recorded "
        "for the Products page. "
        f"Recorded responses: {recorder.responses}"
    )

    products_response = (
        products_responses[-1]
    )

    assert products_response.status == 200, (
        "Expected Products to return HTTP 200, "
        f"but received "
        f"{products_response.status}. "
        f"URL: {products_response.url}"
    )


def test_ui_login_sends_expected_network_payload(
    page: Page,
    home_page: HomePage,
    login_page: LoginPage,
    api_registered_user: Dict[str, str],
) -> None:
    """Verify the UI sends correct login request data."""

    login_page.open()

    expect(
        login_page.login_heading
    ).to_be_visible()

    def is_login_request(
        request: Request,
    ) -> bool:
        return (
            request.method == "POST"
            and has_path(
                request.url,
                "/login",
            )
        )

    def is_login_response(
        response: Response,
    ) -> bool:
        return is_login_request(
            response.request
        )

    with page.expect_request(
        is_login_request,
        timeout=30_000,
    ) as request_info:
        with page.expect_response(
            is_login_response,
            timeout=30_000,
        ) as response_info:
            login_page.login(
                email=api_registered_user[
                    "email"
                ],
                password=api_registered_user[
                    "password"
                ],
            )

    login_request = request_info.value
    login_response = response_info.value

    assert login_request.method == "POST"

    assert login_request.resource_type == (
        "document"
    ), (
        "Expected the login form to submit "
        "a document request, "
        f"but received "
        f"'{login_request.resource_type}'."
    )

    submitted_data = (
        login_request.post_data_json
    )

    assert isinstance(
        submitted_data,
        dict,
    ), (
        "Expected the login request body "
        "to be parsed as a dictionary, "
        f"but received: {submitted_data}"
    )

    assert submitted_data.get("email") == (
        api_registered_user["email"]
    ), (
        "The UI sent an incorrect email. "
        f"Expected: "
        f"{api_registered_user['email']}. "
        f"Received: "
        f"{submitted_data.get('email')}."
    )

    assert submitted_data.get("password") == (
        api_registered_user["password"]
    ), (
        "The UI sent an incorrect password."
    )

    assert (
        200
        <= login_response.status
        < 400
    ), (
        "Expected a successful login response "
        "or redirect, "
        f"but received HTTP "
        f"{login_response.status}. "
        f"URL: {login_response.url}"
    )

    expect(
        home_page.logged_in_as(
            api_registered_user["name"]
        )
    ).to_be_visible()


def test_products_page_has_no_failed_critical_requests(
    page: Page,
    products_page: ProductsPage,
) -> None:
    """Verify no critical first-party requests fail."""

    recorder = NetworkRecorder()
    recorder.start(page)

    products_page.open()

    critical_resource_types = {
        "document",
        "xhr",
        "fetch",
    }

    critical_failures = [
        failed_request
        for failed_request
        in recorder.failed_requests
        if failed_request.resource_type
        in critical_resource_types
    ]

    assert not critical_failures, (
        "Critical first-party network requests "
        "failed while opening Products. "
        f"Failures: {critical_failures}"
    )