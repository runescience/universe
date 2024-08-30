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
