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

#get all records from dynamodb table
def get_all_dynamodb_items(table_name):
    """
    Retrieves all items from the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])
    return items

#pring all records from dynamodb table
def print_all_dynamodb_items(table_name):
    """
    Prints all items from the DynamoDB table
    """
    items = get_all_dynamodb_items(table_name)
    for item in items:
        print(item)


#generic function to get dynamodb item
def get_dynamodb_item(table_name, key):
    """
    Retrieves an item from the DynamoDB table
    """
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response['Item']


      
table_name = 'my_dynamodb_table'
  
#call print_all_dynamodb_items function
print_all_dynamodb_items(table_name)


#call get_dynamodb_item function
key = {
    'id': '1'
}
item = get_dynamodb_item(table_name, key)
print(item)

