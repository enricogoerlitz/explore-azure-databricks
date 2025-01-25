import logging
import json
import azure.functions as func

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient


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
