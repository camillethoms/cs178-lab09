# read_animals.py
# Reads all items from the AlveusAnimals DynamoDB table and prints them.

import boto3

REGION = "us-east-1"
TABLE_NAME = "AlveusAnimals"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_animal(animal):
    name = animal.get("Name", "Unknown")
    species = animal.get("Species", "Unknown Species")
    arrival = animal.get("ArrivalYear", "Unknown Year")

    print(f"  Name        : {name}")
    print(f"  Species     : {species}")
    print(f"  Arrival Year: {arrival}")
    print()

def print_all_animals():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No animals found.")
        return

    print(f"Found {len(items)} animal(s):\n")
    for animal in items:
        print_animal(animal)

def main():
    print("===== Sanctuary Animals =====\n")
    print_all_animals()

if __name__ == "__main__":
    main()
