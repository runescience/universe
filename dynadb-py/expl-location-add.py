import boto3
from botocore.exceptions import ClientError

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

try:
    # Get a reference to the Locations table
    locations_table = dynamodb.Table('Explorer.Location')
    print("Locations table reference obtained successfully.")

except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("Locations table does not exist.")
    else:
        print(f"Error getting Locations table reference: {e}")
    exit(1)  # Exit the program if the table doesn't exist

# Define the location data
location_data = [
    {
        'PK': 'BLACKHOLE#001',
        'X': 26,
        'Y': -5
    },
    {
        'PK': 'BLACKHOLE#002',
        'X': 15,
        'Y': 22
    },
    {
        'PK': 'BLACKHOLE#003',
        'X': -8,
        'Y': -12
    }
]

try:
    # Add the location data to the table
    with locations_table.batch_writer() as batch:
        for location in location_data:
            batch.put_item(Item=location)

    print("Location data added successfully!")

except ClientError as e:
    print(f"Error adding location data to the table: {e}")
