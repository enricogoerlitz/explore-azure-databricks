import logging
import json
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient


# 10.255.1.4 / testing-10-kv.vault.azure.net
KEYVAULT_URL = "https://testing-10-kv.vault.azure.net/"

# 68.219.171.67 / testing-10-cdb.documents.azure.com
COSMOS_DB_ENDPOINT = "https://testing-10-cdb.documents.azure.com/"

COSMOS_DB_DATABASE_NAME = "ToDoList"
COSMOS_DB_CONTAINER_NAME = "Items"

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    access_key = "nothing"
    data = "nothing"

    try:
        logging.info('Processing HTTP request.1')

        # KEY VAULT
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=KEYVAULT_URL, credential=credential)
        access_key = secret_client.get_secret("mykey").value

        # COSMOS
        container = get_cosmosdb_container(access_key)
        items = list(container.query_items(query="SELECT * FROM c", enable_cross_partition_query=True, max_item_count=10))
        data = str(items)
        # created_item = container.create_item(body={"id": "1", "partitionKey": "test"})
        # data = json.dumps(created_item)


    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )

    return func.HttpResponse(
        f"Success: S={access_key}, d={data}",
        status_code=200
    )


def get_cosmosdb_container(access_key: str):
    cosmosdb_client = CosmosClient(COSMOS_DB_ENDPOINT, access_key)
    database = cosmosdb_client.get_database_client(COSMOS_DB_DATABASE_NAME)
    container = database.get_container_client(COSMOS_DB_CONTAINER_NAME)

    return container
