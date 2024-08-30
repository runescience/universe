import boto3
import json

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define the sample JSON data
sample_data = {
    "PK": "OWNER#123",
    "SK": "BEAKCON#678",
    "OwnerName": "Captain Jolly Rogers",
    "OwnerEmail": "john.doe@example.com",
    "MachineModel": "Clingon D7",
    "MachineDescription": "High-performance industrial machine",
    "Parts": [
        {
            "PartName": "Sheilds",
            "PartNumber": "SHd123",
            "Age": 1,
            "Cost": 10000,
            "StructurePoints": 100,
            "Max": 200,
            "ShortName": "SHLD",
            "LongName": "Acme Gear",
            "TechLvl": 1,
            "StartQuan": 4
        },
        {
            "PartName": "DeepMiningRig",
            "PartNumber": "DMR789",
            "Age": 1,
            "Cost": 3,
            "StructurePoints": 80,
            "Max": 150,
            "ShortName": "Mining",
            "LongName": "Deep Mining Rig",
            "TechLvl": 1,
            "StartQuan": 2
        }
    ]
}

# Get the table reference
table = dynamodb.Table('FakeTable')

try:
    # Insert the sample data into the table
    table.put_item(Item=sample_data)
    print("Data inserted successfully!")
except Exception as e:
    print(f"Error inserting data: {e}")
