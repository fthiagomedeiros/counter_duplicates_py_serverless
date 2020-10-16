import json
from src.business_logic.counter_duplicates import counter_duplicates


def counter_duplicates_handler(event, context):
    try:
        data = event['queryStringParameters']['name']
    except:
        return {
            "statusCode": 400,
            "body": 'please, provide query string name'
        }

    output_duplicated_counter = counter_duplicates(data)
    return {
        "statusCode": 200,
        "body": json.dumps(output_duplicated_counter)
    }
