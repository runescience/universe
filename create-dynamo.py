#create dynamodb
import boto3
import time
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def create_dynamodb_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    """
    Creates a DynamoDB table with the given parameters
    """
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )
    return table

#call create_dynamodb_table function
table_name = 'my_dynamodb_table'
key_schema = [
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'
    }
]
attribute_definitions = [
    {
        'AttributeName': 'id',
        'AttributeType': 'S'
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}
table = create_dynamodb_table(table_name, key_schema, attribute_definitions, provisioned_throughput)
print("Table status:", table.table_status)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
print("Table created successfully")

time.sleep(5) #wait for table to be created
print("Table status:", table.table_status)


