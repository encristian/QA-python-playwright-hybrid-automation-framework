from typing import Any, Dict, Optional

import requests
from requests import Response, Session

from utils.config import API_BASE_URL, API_TIMEOUT


class ApiClient:
    """Reusable HTTP client for Automation Exercise APIs."""

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        timeout: int = API_TIMEOUT,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = Session()

        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": (
                    "python-playwright-hybrid-framework/1.0"
                ),
            }
        )

    def build_url(
        self,
        endpoint: str,
    ) -> str:
        """Build the complete URL for an API endpoint."""

        normalized_endpoint = (
            f"/{endpoint.lstrip('/')}"
        )

        return (
            f"{self.base_url}"
            f"{normalized_endpoint}"
        )

    def get(
        self,
        endpoint: str,
        params: Optional[
            Dict[str, Any]
        ] = None,
    ) -> Response:
        """Send a GET request."""

        return self.session.get(
            url=self.build_url(endpoint),
            params=params,
            timeout=self.timeout,
        )

    def post(
        self,
        endpoint: str,
        data: Optional[
            Dict[str, Any]
        ] = None,
        json: Optional[
            Dict[str, Any]
        ] = None,
    ) -> Response:
        """Send a POST request."""

        return self.session.post(
            url=self.build_url(endpoint),
            data=data,
            json=json,
            timeout=self.timeout,
        )

    def put(
        self,
        endpoint: str,
        data: Optional[
            Dict[str, Any]
        ] = None,
        json: Optional[
            Dict[str, Any]
        ] = None,
    ) -> Response:
        """Send a PUT request."""

        return self.session.put(
            url=self.build_url(endpoint),
            data=data,
            json=json,
            timeout=self.timeout,
        )

    def delete(
        self,
        endpoint: str,
        data: Optional[
            Dict[str, Any]
        ] = None,
    ) -> Response:
        """Send a DELETE request."""

        return self.session.delete(
            url=self.build_url(endpoint),
            data=data,
            timeout=self.timeout,
        )

    @staticmethod
    def json_body(
        response: Response,
    ) -> Dict[str, Any]:
        """Parse and validate a JSON response body."""

        try:
            payload = response.json()

        except requests.exceptions.JSONDecodeError as error:
            body_preview = (
                response.text[:300]
                .replace("\n", " ")
            )

            raise AssertionError(
                "Response body is not valid JSON. "
                f"HTTP status: {response.status_code}. "
                f"Body preview: {body_preview}"
            ) from error

        if not isinstance(payload, dict):
            raise AssertionError(
                "Expected the JSON response "
                "to be an object/dictionary, "
                f"but received {type(payload).__name__}."
            )

        return payload

    def close(self) -> None:
        """Close the reusable HTTP session."""

        self.session.close()