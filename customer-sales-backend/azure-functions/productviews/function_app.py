import logging
import json
import azure.functions as func
# import utils

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient
import os


KEYVAULT_URL = os.environ["KEYVAULT_URL"]
COSMOS_DB_ENDPOINT = os.environ["COSMOS_DB_ENDPOINT"]

COSMOS_DB_SECRET_NAME = "cosmos-db-access-key"
COSMOS_DB_DATABASE_NAME = "CustomerSales"
COSMOS_DB_CONTAINER_NAME = "ProductViews"


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


def get_cosmosdb_access_key(
        keyvault_utl: str,
        cosmosdb_db_secret_name: str
) -> str:
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=keyvault_utl, credential=credential)
    access_key = secret_client.get_secret(cosmosdb_db_secret_name).value

    return access_key


def get_cosmosdb_container(
        cosmosdb_endpoint: str,
        cosmosdb_database_name: str,
        cosmosdb_container_name: str,
        access_key: str
):
    cosmosdb_client = CosmosClient(cosmosdb_endpoint, access_key)
    database = cosmosdb_client.get_database_client(cosmosdb_database_name)
    container = database.get_container_client(cosmosdb_container_name)

    return container


def handle_invalid_payload():
    logging.info("Invalid payload.")

    response_json = json.dumps({
        "error": "Invalid payload. Expected: application/json"
    })
    return func.HttpResponse(
        response_json,
        status_code=400,
        mimetype="application/json"
    )


def handle_exception(e, keyvault_url, cosmos_db_endpoint):
    logging.error(f"ENV__KEYVAULT_URL: {keyvault_url}")
    logging.error(f"ENV__COSMOS_DB_ENDPOINT: {cosmos_db_endpoint}")
    logging.error(f"{str(e)}")

    response_json = {
        "error": "An error occurred.",
        "ENV__KEYVAULT_URL": keyvault_url,
        "ENV__COSMOS_DB_ENDPOINT": cosmos_db_endpoint
    }
    return func.HttpResponse(
        response_json,
        status_code=400,
        mimetype="application/json"
    )


cosmosdb_access_key = get_cosmosdb_access_key(
    keyvault_utl=KEYVAULT_URL,
    cosmosdb_db_secret_name=COSMOS_DB_SECRET_NAME
)

container = get_cosmosdb_container(
    cosmosdb_endpoint=COSMOS_DB_ENDPOINT,
    cosmosdb_database_name=COSMOS_DB_DATABASE_NAME,
    cosmosdb_container_name=COSMOS_DB_CONTAINER_NAME,
    access_key=cosmosdb_access_key
)


@app.route(route="productviews", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    created_item = None
    try:
        logging.info("Processing HTTP request")

        payload = req.get_json()
        if not payload:
            return handle_invalid_payload()

        created_item = container.create_item(body=payload)

        response_json = json.dumps(created_item)
        return func.HttpResponse(
            response_json,
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        return handle_exception(e, KEYVAULT_URL, COSMOS_DB_ENDPOINT)
