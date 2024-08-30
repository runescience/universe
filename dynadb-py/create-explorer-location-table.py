import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define the table schema
table_name = 'Explorer.Location'
attribute_definitions = [
    {
        'AttributeName': 'PK',
        'AttributeType': 'S'  # String
    }
]
key_schema = [
    {
        'AttributeName': 'PK',
        'KeyType': 'HASH'  # Partition key
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Drop the table if it already exists
try:
    table = dynamodb.Table(table_name)
    table.delete()
    print(f"Table '{table_name}' deleted successfully.")
except ClientError as e:
    if e.response['Error']['Code'] != 'ResourceNotFoundException':
        print(f"Error deleting table '{table_name}': {e}")
    else:
        print(f"Table '{table_name}' does not exist, skipping deletion.")

# Create the table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        ProvisionedThroughput=provisioned_throughput
    )
    print(f"Table '{table_name}' created successfully!")
except Exception as e:
    print(f"Error creating table '{table_name}': {e}")

