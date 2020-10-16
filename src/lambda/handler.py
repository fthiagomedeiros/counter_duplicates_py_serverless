import json
from src.business_logic.counter_duplicates import counter_duplicates


def counter_duplicates_handler(event, context):
    data = event['queryStringParameters']['name']
    output_duplicated_counter = counter_duplicates(data)

    response = {
        "statusCode": 200,
        "body": json.dumps(output_duplicated_counter)
    }

    return response
