import json
import csv

# Load JSON data
with open('pass_data.json', 'r') as json_file:
    data = json.load(json_file)

headers = [
    'name', 'url', 'email', 'username', 'password', 'note', 'totp', 'vault'
]

# Write to CSV file in Proton Pass format
with open('ProtonPass_data.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for entry in data:
        # Convert each JSON entry to a Proton Pass-compatible row
        writer.writerow({
            'name': entry.get('website', ''),  # Using website as name
            'url': f"https://{entry.get('website', '')}",
            'email': entry.get('username', ''),
            'username': entry.get('username', ''),
            'password': entry.get('password', ''),
            'note': '',
            'totp': '',
            'vault': 'Personal'        # Or another vault name if you wish
        })
