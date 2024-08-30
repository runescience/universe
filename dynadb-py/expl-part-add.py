import boto3
import os

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# get a reference to the Parts table, but if table does not exist catch error

try:
    parts_table = dynamodb.Table('Explorer.Parts')
    print("Parts table reference obtained successfully.")

    # Define the parts data
    parts_data = [
        {
            'PartName': 'shields',
            'Description': 'Provides protection against enemy attacks',
            'Quantity': 4,
            'Damage': 0,
            'TechLevel': 3,
            'StartQuantity': 4
        },
        {
            'PartName': 'engines',
            'Description': 'Propels the ship through space',
            'Quantity': 5,
            'Damage': 0,
            'TechLevel': 2,
            'StartQuantity': 5
        },
        {
            'PartName': 'cargo-slots',
            'Description': 'Holds resources and equipment',
            'Quantity': 100,
            'Damage': 0,
            'TechLevel': 1,
            'StartQuantity': 100
        },
        {
            'PartName': 'missiles',
            'Description': 'Offensive weapons for attacking enemies',
            'Quantity': 2,
            'Damage': 10,
            'TechLevel': 4,
            'StartQuantity': 2
        },
        {
            'PartName': 'mining-rig',
            'Description': 'Extracts resources from asteroids and planets',
            'Quantity': 2,
            'Damage': 0,
            'TechLevel': 3,
            'StartQuantity': 2
        },
        {
            'PartName': 'crew',
            'Description': 'Personnel required to operate the ship',
            'Quantity': 100,
            'Damage': 0,
            'TechLevel': 1,
            'StartQuantity': 100
        }
    ]

    # Add the parts data to the table
    with parts_table.batch_writer() as batch:
        for part in parts_data:
            part_item = {
                'PK': part['PartName'],
                'SK': part['PartName'],
                'Description': part['Description'],
                'Quantity': part['Quantity'],
                'Damage': part['Damage'],
                'TechLevel': part['TechLevel'],
                'StartQuantity': part['StartQuantity']
            }
            batch.put_item(Item=part_item)

    print("Parts data added successfully!")
    
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        print("Parts table does not exist.")
    else:
        print(f"Error getting Parts table reference: {e}")
