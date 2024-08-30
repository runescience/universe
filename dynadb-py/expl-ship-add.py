import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

try:
    # Get a reference to the Ships table
    ships_table = dynamodb.Table('Explorer.Ships')
    print("Ships table reference obtained successfully.")

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("Ships table does not exist.")
    else:
        print(f"Error getting Ships table reference: {e}")
    exit(1)  # Exit the program if the table doesn't exist

# Define the ships data
ships_data = [
    {
        'ShipTag': 'SHIP0001',
        'ShipName': 'Stargazer',
        'PartsList': ['shields', 'engines', 'cargo-slots', 'missiles', 'mining-rig', 'crew']
    },
    # ... (other ships data)
]

try:
    # Add the ships data to the table
    with ships_table.batch_writer() as batch:
        for ship in ships_data:
            ship_item = {
                'PK': ship['ShipTag'],
                'SK': ship['ShipTag'],
                'ShipName': ship['ShipName'],
                'PartsList': ship['PartsList']
            }
            batch.put_item(Item=ship_item)

    print("Ships data added successfully!")

except ClientError as e:
    print(f"Error adding ships data to the table: {e}")
