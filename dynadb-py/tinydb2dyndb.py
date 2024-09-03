import boto3

# Initialize boto3 client
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table
def create_table():
    table = dynamodb.create_table(
        TableName='SpaceObjects',
        KeySchema=[
            {
                'AttributeName': 'xyLocation',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'detailId',
                'KeyType': 'RANGE'  # Sort key for unique objects
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'xyLocation',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'detailId',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    # Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName='SpaceObjects')
    print(f"Table {table.table_name} created successfully.")

    return table

def insert_data():
    # Sample data
    data = [
        {"objects": [], "xyLocation": "0,0"},
        {"objects": [
            {"details": {"ownertag": "SHIP0005", "shipname": "USS Sun Soar", "shipparts": [
                {"partname": "new_engine", "partquan": 3},
                {"partname": "mininig_unit", "partquan": 1}
            ], "shipsize": 9000}, "type": "ship"}], "xyLocation": "6,12"},
        {"objects": [
            {"details": {"ownertag": "SHIP0037", "shipname": "USS Enterprise", "shipparts": [
                {"partname": "engine", "partquan": 2},
                {"partname": "hull", "partquan": 1},
                {"partname": "crew", "partquan": 100}
            ], "shipsize": 1000}, "type": "ship"}], "xyLocation": "66,77"},
        {"objects": [], "xyLocation": "12,34"},
        {"objects": [
            {"details": {"ownertag": "SHIP0100", "shipname": "USS New Voyager", "shipparts": [
                {"partname": "warp_drive", "partquan": 2},
                {"partname": "laser_cannons", "partquan": 4},
                {"partname": "mining_drones", "partquan": 2},
                {"partname": "shields", "partquan": 5},
                {"partname": "hull", "partquan": 18},
                {"partname": "ecm", "partquan": 1},
                {"partname": "bulkhead", "partquan": 10},
                {"partname": "short_scanner", "partquan": 1},
                {"partname": "pe", "partquan": 1000},
                {"partname": "spares", "partquan": 20},
                {"partname": "eng", "partquan": 8},
                {"partname": "screens", "partquan": 6},
                {"partname": "short_scanner", "partquan": 20},
                {"partname": "long_scanner", "partquan": 1},
                {"partname": "worm_points", "partquan": 2},
                {"partname": "shield_booster", "partquan": 4},
                {"partname": "worm_points", "partquan": 2},
                {"partname": "shield_booster", "partquan": 4}
            ], "shipsize": 7500}, "type": "ship"}], "xyLocation": "34,56"},
        {"objects": [
            {"details": {"ownertag": "SHIP9871", "shipname": "USS Sun Soar", "shipparts": [], "shipsize": 0}, "type": "ship"}], "xyLocation": "6,12"}
    ]

    table = dynamodb.Table('SpaceObjects')

    for item in data:
        for obj in item['objects']:
            details = obj['details']
            table.put_item(Item={
                'xyLocation': item['xyLocation'],
                'detailId': details['ownertag'],
                'shipname': details['shipname'],
                'shipsize': details['shipsize'],
                'shipparts': details['shipparts']
            })
    print(f"Data inserted successfully.")

if __name__ == '__main__':
    create_table()
    insert_data()