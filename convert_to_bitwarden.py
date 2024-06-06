import json
import csv

pass_data = []
with open("./pass_data.json", "r") as f:
    pass_data = json.load(f)
    
def convert_to_bitwarden(entries: list):
    bitwarden_entries = []
    for entry in entries:
        bitwarden_entry = {
            "folder": "",
            "favorite": "",
            "type": "login",
            "name": entry["website"],
            "notes": "",
            "fields": "",
            "reprompt": 0,
            "login_uri": entry["website"],
            "login_username": entry["username"],
            "login_password": entry["password"],
            "login_totp": ""
        }
        bitwarden_entries.append(bitwarden_entry)
    return bitwarden_entries

if __name__ == "__main__":
    pass_data = []
    with open("./pass_data.json", "r") as f:
        pass_data = json.load(f)
    
    bitwarden_entries = convert_to_bitwarden(pass_data)
    
    # write the data to a csv file
    with open("./bitwarden_data.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["folder", "favorite", "type", "name", "notes", "fields", "reprompt", "login_uri", "login_username", "login_password", "login_totp"])
        writer.writeheader()
        writer.writerows(bitwarden_entries)
