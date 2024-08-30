import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define the table schema
table_name = 'SpaceObjects'
attribute_definitions = [
    {'AttributeName': 'PK', 'AttributeType': 'S'},
    {'AttributeName': 'SK', 'AttributeType': 'S'}
]
key_schema = [
    {'AttributeName': 'PK', 'KeyType': 'HASH'},
    {'AttributeName': 'SK', 'KeyType': 'RANGE'}
]
provisioned_throughput = {
    'ReadCapacityUnits': 10,
    'WriteCapacityUnits': 10
}

# Create the table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        ProvisionedThroughput=provisioned_throughput
    )
    table.wait_until_exists()
    print(f"Table '{table_name}' created successfully!")
except Exception as e:
    print(f"Error creating table: {e}")
