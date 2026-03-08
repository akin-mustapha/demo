import boto3
import json

with open("../access_key.json", "r") as f:
    access_key = json.load(f)
    access_key_id = access_key["aws_access_key_id"]
    secret_access_key = access_key["aws_secret_access_key"]

dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-north-1",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    # endpoint_url="http://localhost:8000",
)


table = dynamodb.Table('tbl_test_1')

table.put_item(
    Item={
        'file_type': 'pdf',
        'file_name': 'test_2.pdf'
    }
)



print(table)