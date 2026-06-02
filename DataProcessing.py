import csv
import json

# Read data from CSV file
data = []

with open("students.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        # Process data (convert marks to integer)
        row["Marks"] = int(row["Marks"])
        data.append(row)

# Store processed data in JSON file
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Data processed and saved to students.json successfully!")
