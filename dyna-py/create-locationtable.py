import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define the table schema
table_name = 'location_table'
attribute_definitions = [
    {'AttributeName': 'MachineTAG', 'AttributeType': 'S'}
]
key_schema = [
    {'AttributeName': 'MachineTAG', 'KeyType': 'HASH'}
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        ProvisionedThroughput=provisioned_throughput
    )
    table.wait_until_exists()
    print(f"Table '{table_name}' created successfully!")
except Exception as e:
    print(f"Error creating table: {e}")

# Get the table references
fake_table = dynamodb.Table('FakeTable')
location_table = dynamodb.Table('location_table')

# Fetch data from the FakeTable
response = fake_table.scan()
items = response['Items']

# Insert data into the location_table
for item in items:
    machine_tag = item['SK']
    xx = 10  # Replace with the desired xx value
    yy = 10  # Replace with the desired yy value
    
    location_data = {
        'MachineTAG': machine_tag,
        'xx': xx,
        'yy': yy
    }
    
    try:
        location_table.put_item(Item=location_data)
        print(f"Location data inserted for machine {machine_tag}")
    except Exception as e:
        print(f"Error inserting location data for machine {machine_tag}: {e}")
