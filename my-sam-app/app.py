import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    data = json.loads(event['body'])
    data['id'] = str(uuid.uuid4())
    table.put_item(Item=data)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data inserted successfully!', 'data': data})
    }
