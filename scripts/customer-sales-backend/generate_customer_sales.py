# flake8: noqa

import random
import requests

from uuid import uuid4


IS_LOCAL = True

ORDER_COUNT = 2

CUSTOMER_SALES_HOST = "https://eadb-dev-weu-ca.niceforest-817f97fb.westeurope.azurecontainerapps.io" # "http://localhost:8080"

CUSTOMER_SALES_SERVICE_ROUTE = "customersales/api/v1" if not IS_LOCAL else "api/v1"
CUSTOMER_SALES_ENDPOINT = f"{CUSTOMER_SALES_HOST}/{CUSTOMER_SALES_SERVICE_ROUTE}"


def get_user_ids(offset: int, limit: int) -> list[int]:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/users?offset={offset}&limit={limit}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return [user["ID"] for user in response.json()]
    else:
        return []


def create_users(count: int) -> None:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/users"
    for _ in range(count):
        data = {
            "Firstname": "firstname",
            "Lastname": str(uuid4().hex),
            "Password": "blub"
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 201:
            print("User created successfully")
        else:
            print("Failed to create user")


def update_users(user_ids: list[int]) -> None:
    for user_id in user_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/users/{user_id}"
        data = {
            "Lastname": uuid4().hex,
        }
        response = requests.patch(endpoint, json=data)
        if response.status_code == 200:
            print("User updated successfully")
        else:
            print("Failed to update user")


def delete_users(user_ids: list[int]) -> None:
    for user_id in user_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/users/{user_id}"
        requests.delete(endpoint)
        print(f"Usser ID: {user_id} deleted")


def get_distributor_ids(offset: int, limit: int) -> list[int]:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/distributors?offset={offset}&limit={limit}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return [distributor["ID"] for distributor in response.json()]
    else:
        return []


def create_distributors(count: int) -> None:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/distributors"
    for _ in range(count):
        data = {
            "Name": f"distributor-{str(uuid4().hex)}",
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 201:
            print("Distributor created successfully")
        else:
            print("Failed to create distributor")


def update_distributors(distributor_ids: list[int]) -> None:
    for distributor_id in distributor_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/distributors/{distributor_id}"
        data = {
            "Name": f"distributor-{str(uuid4().hex)}"
        }
        response = requests.patch(endpoint, json=data)
        if response.status_code == 200:
            print("Distributor updated successfully")
        else:
            print("Failed to update distributor")


def delete_distributors(distributor_ids: list[int]) -> None:
    for distributor_id in distributor_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/distributors/{distributor_id}"
        requests.delete(endpoint)
        print(f"Distributor ID: {distributor_id} deleted")


def get_product_ids(offset: int, limit: int) -> list[int]:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/products?offset={offset}&limit={limit}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return [product["ID"] for product in response.json()]
    else:
        return []


def create_products(count: int, distributor_ids: list[int], category_ids: list[int]) -> None:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/products"

    if len(distributor_ids) == 0 or len(category_ids) == 0:
        return

    for _ in range(count):
        data = {
            "Name": f"product-{str(uuid4().hex)}",
            "Description": "lorem ipsum",
            "Price": 500,
            "CategoryID": random.choice(category_ids),
            "DistributorID": random.choice(distributor_ids)
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 201:
            print("Product created successfully")
        else:
            print("Failed to create product")


def update_products(product_ids: list[int]) -> None:
    for product_id in product_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/products/{product_id}"
        data = {
            "Name": f"product-u-{str(uuid4().hex)}"
        }
        response = requests.patch(endpoint, json=data)
        if response.status_code == 200:
            print("Product updated successfully")
        else:
            print("Failed to update product")


def delete_products(product_ids: list[int]) -> None:
    for product_id in product_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/products/{product_id}"
        requests.delete(endpoint)
        print(f"Product ID: {product_id} deleted")


def get_region_ids(offset: int, limit: int) -> list[int]:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/regions?offset={offset}&limit={limit}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return [region["ID"] for region in response.json()]
    else:
        return []


def create_regions(count: int) -> None:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/regions"
    for _ in range(count):
        data = {
            "Name": f"region-{str(uuid4().hex)}",
            "Long": 0,
            "Lat": 0
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 201:
            print("Region created successfully")
        else:
            print("Failed to create region")


def update_regions(region_ids: list[int]) -> None:
    for region_id in region_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/regions/{region_id}"
        data = {
            "Name": f"region-{str(uuid4().hex)}",
        }
        response = requests.patch(endpoint, json=data)
        if response.status_code == 200:
            print("Region updated successfully")
        else:
            print("Failed to update region")


def delete_regions(region_ids: list[int]) -> None:
    for region_id in region_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/regions/{region_id}"
        requests.delete(endpoint)
        print(f"Region ID: {region_id} deleted")


def get_product_category_ids(offset: int, limit: int) -> list[int]:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/product-categories?offset={offset}&limit={limit}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return [category["ID"] for category in response.json()]
    else:
        return []


def create_product_categories(count: int) -> None:
    endpoint = f"{CUSTOMER_SALES_ENDPOINT}/product-categories"
    for _ in range(count):
        data = {
            "Name": f"category-{str(uuid4().hex)}",
            "Description": "description"
        }
        response = requests.post(endpoint, json=data)
        if response.status_code == 201:
            print("Product category created successfully")
        else:
            print("Failed to create product category")


def update_product_categories(category_ids: list[int]) -> None:
    for category_id in category_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/product-categories/{category_id}"
        data = {
            "Name": f"category-{str(uuid4().hex)}"
        }
        response = requests.patch(endpoint, json=data)
        if response.status_code == 200:
            print("Product category updated successfully")
        else:
            print("Failed to update product category")


def delete_product_categories(category_ids: list[int]) -> None:
    for category_id in category_ids:
        endpoint = f"{CUSTOMER_SALES_ENDPOINT}/product-categories/{category_id}"
        requests.delete(endpoint)
        print(f"Category ID: {category_id} deleted")


def create_orders(
        count: int,
        user_ids: list[int],
        region_ids: list[int],
        product_ids: list[int]
) -> None:
    orders_endpoint = f"{CUSTOMER_SALES_ENDPOINT}/orders"
    for i in range(count):
        order = {
            "UserID": random.choice(user_ids),
            "DestinationRegionID": random.choice(region_ids),
            "TotalPrice": random.randint(100, 1000),
            "Status": "blub"
        }

        response = requests.post(orders_endpoint, json=order)
        order_resp = response.json()

        order_id = order_resp["ID"]
        order_item_endpoint = f"{orders_endpoint}/{order_id}/items"

        print("ORDER ID: ", order_id, "ORDER ITER: ", i)
        for _ in range(random.randint(10, 50)):
            order_item = {
                "ProductID": random.choice(product_ids),
                "ProductPrice": random.randint(25, 150),
                "Quantity": random.randint(1, 10),
                "Status": "blub"
            }
            response = requests.post(order_item_endpoint, json=order_item)


if __name__ == "__main__":
    create_distributors(110)
    create_users(250)
    create_regions(110)
    create_product_categories(200)

    user_ids = get_user_ids(0, 100)
    category_ids = get_product_category_ids(0, 100)
    distributor_ids = get_distributor_ids(0, 100)
    region_ids = get_region_ids(0, 100)

    delete_user_ids = get_user_ids(100, 100)
    delete_category_ids = get_product_category_ids(100, 100)
    delete_distributor_ids = get_distributor_ids(100, 100)
    delete_region_ids = get_region_ids(100, 100)

    create_products(300, distributor_ids, category_ids)

    product_ids = get_product_ids(0, 100)
    delete_product_ids = get_product_ids(100, 100)

    create_orders(ORDER_COUNT, user_ids, region_ids, product_ids)

    update_distributors(random.sample(distributor_ids, 10))
    update_users(random.sample(user_ids, 10))
    update_products(random.sample(product_ids, 10))
    update_regions(random.sample(region_ids, 10))
    update_product_categories(random.sample(category_ids, 10))

    delete_products(random.sample(delete_product_ids, 3))
    delete_distributors(random.sample(delete_distributor_ids, 3))
    delete_users(random.sample(delete_user_ids, 3))
    delete_regions(random.sample(delete_region_ids, 3))
    delete_product_categories(random.sample(delete_category_ids, 3))

    