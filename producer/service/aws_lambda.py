import boto3
import json
import logging
from producer.config.config import config

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

region = config["aws"]["region"]
function_name = config["aws"]["lambda_function_name"]

lambda_client = boto3.client("lambda", region_name=region)

def invoke_lambda(payload: dict, function_name_override: str = None):
    try:
        fn = function_name_override or function_name
        response = lambda_client.invoke(
            FunctionName=fn,
            InvocationType="Event",
            Payload=json.dumps(payload)
        )
        logger.info(f"Lambda invoked: {response}")
        return response
    except Exception as e:
        logger.error(f"Error invoking Lambda: {e}")
        raise
