import logging
import json
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient
import os


KEYVAULT_URL = os.environ["KEYVAULT_URL"]
COSMOS_DB_ENDPOINT = os.environ["COSMOS_DB_ENDPOINT"]

COSMOS_DB_SECRET_NAME = "cosmos-db-access-key-2"
COSMOS_DB_DATABASE_NAME = "CustomerSales"
COSMOS_DB_CONTAINER_NAME = "ProductViews"


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


def get_cosmosdb_access_key() -> str:
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=KEYVAULT_URL, credential=credential)
    access_key = secret_client.get_secret(COSMOS_DB_SECRET_NAME).value

    return access_key


def get_cosmosdb_container(access_key: str):
    cosmosdb_client = CosmosClient(COSMOS_DB_ENDPOINT, access_key)
    database = cosmosdb_client.get_database_client(COSMOS_DB_DATABASE_NAME)
    container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)

    return container


@app.route(route="productviews", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    created_item = None
    try:
        logging.info("Processing HTTP request")

        payload = req.get_json()
        if not payload:
            logging.info("Invalid payload.")

            response_json = json.dumps({
                "error": "Invalid payload. Expected: application/json"
            })
            return func.HttpResponse(
                response_json,
                status_code=400,
                mimetype="application/json"
            )

        cosmosdb_access_key = get_cosmosdb_access_key()
        container = get_cosmosdb_container(cosmosdb_access_key)

        created_item = container.create_item(body=payload)

        response_json = json.dumps(created_item)
        return func.HttpResponse(
            response_json,
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"ENV__KEYVAULT_URL: {KEYVAULT_URL}")
        logging.error(f"ENV__COSMOS_DB_ENDPOINT: {COSMOS_DB_ENDPOINT}")
        logging.error(f"{str(e)}")

        response_json = {
            "error": "An error occurred.",
            "ENV__KEYVAULT_URL": KEYVAULT_URL,
            "ENV__COSMOS_DB_ENDPOINT": COSMOS_DB_ENDPOINT
        }
        return func.HttpResponse(
            json.dumps(response_json),
            status_code=400,
            mimetype="application/json"
        )
