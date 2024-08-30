import boto3
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
logging.info("DynamoDB resource created.")

# Get references to the SpaceObjects, Explorer.Location, and Explorer.Ships tables
space_objects_table = dynamodb.Table('Explorer.SpaceObjects')
location_table = dynamodb.Table('Explorer.Location')
ships_table = dynamodb.Table('Explorer.Ships')
logging.info("Table references obtained.")

# Define the space object types and their coordinate ranges
object_types = {
    'PLANET': (-10, 10),
    'ASTEROID': (10, 50),
    'BLACKHOLE': (50, 100),
    'STAR': (-50, 50)
}

# Generate sample space object data
space_objects = []
locations = []
ships = []
logging.info("Starting data generation...")
for i in range(1, 101):
    object_type = random.choice(list(object_types.keys()))
    x_range = object_types[object_type]
    x = random.randint(x_range[0], x_range[1])
    y = random.randint(x_range[0], x_range[1])
    object_tag = f'{object_type}#{i:03}'
    space_objects.append({
        'PK': f'OBJECT#{object_type}',
        'SK': object_tag,
        'Name': f'{object_type} {i:03}',
        'Type': object_type
    })
    locations.append({
        'PK': object_tag,
        'X': x,
        'Y': y
    })
    ships.append({
        'PK': f'SHIP#{i:03}',
        'SK': f'SHIP#{i:03}',
        'Name': f'Ship {i:03}',
        'Parts': [f'Part {i:03}-1', f'Part {i:03}-2', f'Part {i:03}-3']
    })
logging.info("Data generation completed.")

# Add the space object data to the Explorer.SpaceObjects table
logging.info("Adding data to Explorer.SpaceObjects table...")
with space_objects_table.batch_writer() as batch:
    for obj in space_objects:
        batch.put_item(Item=obj)
logging.info("Data added to Explorer.SpaceObjects table.")

# Add the location data to the Explorer.Location table
logging.info("Adding data to Explorer.Location table...")
with location_table.batch_writer() as batch:
    for loc in locations:
        batch.put_item(Item=loc)
logging.info("Data added to Explorer.Location table.")

# Add the ship data to the Explorer.Ships table
logging.info("Adding data to Explorer.Ships table...")
with ships_table.batch_writer() as batch:
    for ship in ships:
        batch.put_item(Item=ship)
logging.info("Data added to Explorer.Ships table.")

logging.info("Space object, location, and ship data added successfully!")
