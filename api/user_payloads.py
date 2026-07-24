from typing import Dict


def build_account_payload(
    user: Dict[str, str],
) -> Dict[str, str]:
    """Convert generated user data to the API format."""

    return {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "title": user["title"],
        "birth_date": user["birth_day"],
        "birth_month": user["birth_month"],
        "birth_year": user["birth_year"],
        "firstname": user["first_name"],
        "lastname": user["last_name"],
        "company": user["company"],
        "address1": user["address"],
        "address2": user["address2"],
        "country": user["country"],
        "zipcode": user["zipcode"],
        "state": user["state"],
        "city": user["city"],
        "mobile_number": user["mobile_number"],
    }


def build_credentials(
    user: Dict[str, str],
) -> Dict[str, str]:
    """Return the email and password of a user."""

    return {
        "email": user["email"],
        "password": user["password"],
    }