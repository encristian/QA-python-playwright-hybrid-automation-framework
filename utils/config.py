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