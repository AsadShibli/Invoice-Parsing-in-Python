import json
import csv

# Load JSON data
with open("response1.json", "r") as f:
    data = json.load(f)

# Print receipt items
for item in data["receipts"][0]["items"]:
    description = item["description"]
    amount = item["amount"]
    unit_price = item["unitPrice"]
    quantity = amount / unit_price
    print(f"Description: {description}, Price: {amount}, Quantity: {quantity}, Unit Price: {unit_price}")

# Create CSV file
csv_file = "receipt_items.csv"
csv_columns = ["Description", "Price", "Quantity", "Unit Price"]

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for item in data["receipts"][0]["items"]:
            writer.writerow({
                "Description": item["description"],
                "Price": item["amount"],
                "Quantity": item["amount"] / item["unitPrice"],
                "Unit Price": item["unitPrice"]
            })
    print(f"CSV file '{csv_file}' created successfully.")
except IOError:
    print("I/O error")
