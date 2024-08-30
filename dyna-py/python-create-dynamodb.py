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
time.sleep(5) #wait for table to be created
print("Table status:", table.table_status)


#getdynamodb
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def get_dynamodb_table(table_name):
    """
    Retrieves the DynamoDB table with the given name
    """
    table = dynamodb.Table(table_name)
    return table
#call get_dynamodb_table function
table_name = 'my_dynamodb_table'
table = get_dynamodb_table(table_name)
print("Table status:", table.table_status)


#putdynamodb
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def put_dynamodb_item(table_name, item):
    """
    Puts an item into the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)
    return table

#call put_dynamodb_item function
table_name = 'my_dynamodb_table'
item = {
    'id': '1',
    'name': 'John Doe',
    'age': 30
}
table = put_dynamodb_item(table_name, item)
print("Table status:", table.table_status)


#getdynamodb
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def get_dynamodb_item(table_name, key):
    """
    Retrieves an item from the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response['Item']
#call get_dynamodb_item function
table_name = 'my_dynamodb_table'
key = {
    'id': '1'
}
item = get_dynamodb_item(table_name, key)
print(item)


#updatedynamodb
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def update_dynamodb_item(table_name, key, update_expression, expression_attribute_values):
    """
    Updates an item in the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    return response
#call update_dynamodb_item function
table_name = 'my_dynamodb_table'
key = {
    'id': '1'
}
update_expression = 'SET age = :new_age'
expression_attribute_values = {
    ':new_age': 31
}
response = update_dynamodb_item(table_name, key, update_expression, expression_attribute_values)
print("Update response:", response)

#deletedynamodb
import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
def delete_dynamodb_item(table_name, key):
    """
    Deletes an item from the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    table.delete_item(Key=key)
    return table
