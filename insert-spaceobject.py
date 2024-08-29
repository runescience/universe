import boto3
import json

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Get the table reference
table = dynamodb.Table('SpaceObjects')

# Define the sample JSON data
sample_data = [
    {
        'PK': 'SHIP#SHIP123456',
        'SK': 'DETAILS',
        'ShipName': 'Starship Voyager',
        'ShipTag': 'SHIP123456'
    },
    {
        'PK': 'SHIP#SHIP123456',
        'SK': 'PARTS',
        'Parts': [
            {
                'ShortName': 'sh',
                'Description': 'Shields',
                'Quantity': 4,
                'Damage': 0,
                'TechLvl': 5,
                'StartQuan': 4
            },
            {
                'ShortName': 'en',
                'Description': 'Engines',
                'Quantity': 5,
                'Damage': 0,
                'TechLvl': 4,
                'StartQuan': 5
            }
        ]
    },
    {
        'PK': 'SHIP#SHIP123456',
        'SK': 'LOCATION',
        'xx': 100,
        'yy': 200
    },
    {
        'PK': 'HAZARD#HAZARD789',
        'SK': 'DETAILS',
        'HazardName': 'Asteroid Field',
        'HazardDescription': 'Dangerous asteroid field'
    },
    {
        'PK': 'HAZARD#HAZARD789',
        'SK': 'LOCATION',
        'xx': 300,
        'yy': 400
    }
]

# Insert the sample data into the table
for item in sample_data:
    try:
        table.put_item(Item=item)
        print(f"Data inserted successfully: {item}")
    except Exception as e:
        print(f"Error inserting data: {e}")
