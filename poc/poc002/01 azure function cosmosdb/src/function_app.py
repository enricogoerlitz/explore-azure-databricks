import logging
import json
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient


KEYVAULT_URL = "https://testingdevweukv.vault.azure.net/"

COSMOS_DB_ENDPOINT = "https://poc002-dev-weu-cdb2.documents.azure.com:443/"
COSMOS_DB_DATABASE_NAME = "ToDoList"
COSMOS_DB_CONTAINER_NAME = "Items"


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    access_key = "nothing"
    container_str = "nothing"
    payload = "nothing"
    list_items = "nothing"
    try:
        logging.info('Processing HTTP request.')

        payload = req.get_json()
        if not payload:
            return func.HttpResponse("Invalid payload", status_code=400)

        # KEY VAULT
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=KEYVAULT_URL, credential=credential)
        access_key = secret_client.get_secret("cosmosdb-access-key").value

        # COSMOS DB
        cosmosdb_client = CosmosClient(COSMOS_DB_ENDPOINT, access_key)
        database = cosmosdb_client.get_database_client(COSMOS_DB_DATABASE_NAME)
        container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)
        container_str = str(container)

        container.create_item(body=payload)

        items = list(container.query_items(query="SELECT * FROM c", enable_cross_partition_query=True, max_item_count=10))
        list_items = str(items)

    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )

    return func.HttpResponse(
        f"Success: S={container_str}, LI={str(list_items)}, O={str(payload)}",
        status_code=200
    )
