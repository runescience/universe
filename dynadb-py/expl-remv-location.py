import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
logging.info("DynamoDB resource created.")

# Get a reference to the Explorer.Ships table
ships_table = dynamodb.Table('Explorer.Ships')
logging.info("Table reference obtained.")

# Scan the Explorer.Ships table and remove the Location attribute
logging.info("Scanning Explorer.Ships table...")
response = ships_table.scan()
with ships_table.batch_writer() as batch:
    for item in response['Items']:
        if 'Location' in item:
            del item['Location']
            batch.put_item(Item=item)
            logging.info(f"Removed Location attribute from item: {item['PK']}")

# Check for any remaining items in the response
while 'LastEvaluatedKey' in response:
    response = ships_table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    with ships_table.batch_writer() as batch:
        for item in response['Items']:
            if 'Location' in item:
                del item['Location']
                batch.put_item(Item=item)
                logging.info(f"Removed Location attribute from item: {item['PK']}")

logging.info("Location attribute removed from all items in Explorer.Ships table.")
