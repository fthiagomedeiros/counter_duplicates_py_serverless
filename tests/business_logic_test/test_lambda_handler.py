from mock import patch
from src.lambdas.handler import counter_duplicates_handler


@patch('src.business_logic.counter_duplicates')
def test_counter_duplicates_handler(counter_duplicates_mock):
    event = {"queryStringParameters": {"name": "abca"}}
    counter_duplicates_mock.return_value = {'a': 2}

    resp = counter_duplicates_handler(event, None)
    assert resp == {'statusCode': 200, 'body': '{"a": 2}'}
