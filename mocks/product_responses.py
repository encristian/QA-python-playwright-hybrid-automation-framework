from typing import Any, Dict, List


MOCK_PRODUCTS: List[Dict[str, Any]] = [
    {
        "id": 9001,
        "name": "Mocked Blue Hoodie",
        "price": "Rs. 1500",
        "brand": "Mock Fashion",
        "category": {
            "usertype": {
                "usertype": "Women",
            },
            "category": "Tops",
        },
    },
    {
        "id": 9002,
        "name": "Mocked Black Jeans",
        "price": "Rs. 2200",
        "brand": "Mock Denim",
        "category": {
            "usertype": {
                "usertype": "Men",
            },
            "category": "Jeans",
        },
    },
]


MOCK_PRODUCTS_RESPONSE: Dict[str, Any] = {
    "responseCode": 200,
    "products": MOCK_PRODUCTS,
}


MOCK_SERVER_ERROR_RESPONSE: Dict[str, Any] = {
    "responseCode": 500,
    "message": "Mocked internal server error.",
}