import boto3
import json

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define the sample JSON data
sample_data = {
    "PK": "OWNER#123",
    "SK": "MACHINE#456",
    "OwnerName": "John Doe",
    "OwnerEmail": "john.doe@example.com",
    "MachineModel": "Acme 2000",
    "MachineDescription": "High-performance industrial machine",
    "Parts": [
        {
            "PartName": "Gear",
            "PartNumber": "ABC123",
            "Age": 2,
            "Cost": 20,
            "StructurePoints": 100,
            "Max": 200,
            "ShortName": "Gear",
            "LongName": "Acme Gear",
            "TechLvl": 5,
            "StartQuan": 10
        },
        {
            "PartName": "Bearing",
            "PartNumber": "XYZ456",
            "Age": 1,
            "Cost": 3,
            "StructurePoints": 80,
            "Max": 150,
            "ShortName": "Bearing",
            "LongName": "Acme Bearing",
            "TechLvl": 4,
            "StartQuan": 20
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
