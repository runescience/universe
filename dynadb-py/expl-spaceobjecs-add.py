import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

try:
    # Get a reference to the SpaceObjects table
    space_objects_table = dynamodb.Table('Explorer.SpaceObjects')
    print("SpaceObjects table reference obtained successfully.")

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("SpaceObjects table does not exist.")
    else:
        print(f"Error getting SpaceObjects table reference: {e}")
    exit(1)  # Exit the program if the table doesn't exist

# Define the space objects data
space_objects_data = [
    {
        'PK': 'OBJECT#PLANET',
        'SK': 'PLANET#002',
        'Name': 'Earth',
        'Type': 'Planet'
    },
    {
        'PK': 'OBJECT#ASTEROID',
        'SK': 'ASTEROID#002',
        'Name': 'Ceres',
        'Type': 'Asteroid',
    },
    {
        'PK': 'OBJECT#BLACKHOLE',
        'SK': 'BLACKHOLE#002',
        'Name': 'Sagittarius A*',
        'Type': 'Black Hole'
    }
]

try:
    # Add the space objects data to the table
    with space_objects_table.batch_writer() as batch:
        for obj in space_objects_data:
            batch.put_item(Item=obj)

    print("Space objects data added successfully!")

except ClientError as e:
    print(f"Error adding space objects data to the table: {e}")
