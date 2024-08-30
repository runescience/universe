import boto3
import random

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Get references to the SpaceObjects and Explorer.Location tables
space_objects_table = dynamodb.Table('Explorer.SpaceObjects')
location_table = dynamodb.Table('Explorer.Location')

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

# Add the space object data to the SpaceObjects table
with space_objects_table.batch_writer() as batch:
    for obj in space_objects:
        batch.put_item(Item=obj)

# Add the location data to the Explorer.Location table
with location_table.batch_writer() as batch:
    for loc in locations:
        batch.put_item(Item=loc)

print("Space object and location data added successfully!")
