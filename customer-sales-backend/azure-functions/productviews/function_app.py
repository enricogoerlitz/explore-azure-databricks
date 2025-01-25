import logging
import json
import azure.functions as func
import os
import utils


KEYVAULT_URL = os.environ["KEYVAULT_URL"]
COSMOS_DB_ENDPOINT = os.environ["COSMOS_DB_ENDPOINT"]

COSMOS_DB_SECRET_NAME = "cosmos-db-access-key"
COSMOS_DB_DATABASE_NAME = "CustomerSales"
COSMOS_DB_CONTAINER_NAME = "ProductViews"


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


cosmosdb_access_key = utils.get_cosmosdb_access_key(
    keyvault_utl=KEYVAULT_URL,
    cosmosdb_db_secret_name=COSMOS_DB_SECRET_NAME
)

container = utils.get_cosmosdb_container(
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
            return utils.handle_invalid_payload()

        created_item = container.create_item(body=payload)

        response_json = json.dumps(created_item)
        return func.HttpResponse(
            response_json,
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        return utils.handle_exception(e, KEYVAULT_URL, COSMOS_DB_ENDPOINT)
