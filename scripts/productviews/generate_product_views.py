import requests
import random


VIEWS_COUNT = 10_000

CUSTOMER_SALES_HOST = ""
PRODUCT_VIEWS_ENDPOINT = ""

CUSTOMER_SALES_ENDPOINT = f"{CUSTOMER_SALES_HOST}/customersales/api/v1"


def fetch_product_ids() -> list[int]:
    products_endpoint = f"{CUSTOMER_SALES_ENDPOINT}/products"
    try:
        response = requests.get(products_endpoint)
        response.raise_for_status()
        return [product["ID"] for product in response.json()]
    except Exception as e:
        print(e)
        raise e


def fetch_user_ids() -> list[int]:
    users_endpoint = f"{CUSTOMER_SALES_ENDPOINT}/users"
    try:
        response = requests.get(users_endpoint)
        response.raise_for_status()
        return [user["ID"] for user in response.json()]
    except Exception as e:
        print(e)
        raise e


def generate_product_view(
        product_id: int,
        user_id: int,
) -> None:
    data = {
        "product_id": product_id,
        "user_id": user_id,
    }
    try:
        response = requests.post(PRODUCT_VIEWS_ENDPOINT, data=data)
        response.raise_for_status()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    product_ids = fetch_product_ids()
    user_ids = fetch_user_ids()

    for _ in range(VIEWS_COUNT):
        product_id = random.choice(product_ids)
        user_id = random.choice(user_ids)
        generate_product_view(product_id, user_id)
