import os

from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv(
    "BASE_URL",
    "https://automationexercise.com",
).rstrip("/")

DEFAULT_TIMEOUT = int(
    os.getenv(
        "DEFAULT_TIMEOUT",
        "60000",
    )
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    f"{BASE_URL}/api",
).rstrip("/")

API_TIMEOUT = int(
    os.getenv(
        "API_TIMEOUT",
        "30",
    )
)