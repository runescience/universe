import boto3

# Create a DynamoDB resource with the desired region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Replace with your desired region

# Define the table schema
table_name = 'OwnerMachinesParts'
attribute_definitions = [
    {'AttributeName': 'PK', 'AttributeType': 'S'},
    {'AttributeName': 'SK', 'AttributeType': 'S'}
]
key_schema = [
    {'AttributeName': 'PK', 'KeyType': 'HASH'},
    {'AttributeName': 'SK', 'KeyType': 'RANGE'}
]
global_secondary_indexes = [
    {
        'IndexName': 'GSI_OwnerMachines',
        'KeySchema': [
            {'AttributeName': 'PK', 'KeyType': 'HASH'},
            {'AttributeName': 'SK', 'KeyType': 'RANGE'}
        ],
        'Projection': {
            'ProjectionType': 'INCLUDE',
            'NonKeyAttributes': ['MachineModel', 'MachineDescription']
        },
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    },
    {
        'IndexName': 'GSI_MachineParts',
        'KeySchema': [
            {'AttributeName': 'PK', 'KeyType': 'HASH'},
            {'AttributeName': 'SK', 'KeyType': 'RANGE'}
        ],
        'Projection': {
            'ProjectionType': 'INCLUDE',
            'NonKeyAttributes': ['Age', 'Cost', 'StructurePoints', 'Max', 'ShortName', 'LongName', 'TechLvl', 'StartQuan']
        },
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    }
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
try:
    
    table = dynamodb.create_table(
        TableName='FakeTable',
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        GlobalSecondaryIndexes=global_secondary_indexes,
        ProvisionedThroughput=provisioned_throughput
    )
    
    table.wait_until_exists()
    print(f"Table '{table_name}' created successfully!")
except Exception as e:
    print(f"Error creating table: {e}")
