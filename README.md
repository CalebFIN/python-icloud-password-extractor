# iCloud Password Entry Extractor

This Python script automates the process of extracting password entries from a specific application and saves them in a structured JSON format. It uses the `pywinauto` library to control and interact with Windows applications, and `pyperclip` for clipboard operations.

## Features

- **Automated Extraction**: Automatically navigates through password entries in the target application.
- **De-duplication**: Ensures that the extracted data does not contain duplicate entries.
- **Data Structuring**: Structures the extracted data into a readable and manageable JSON format.

## Requirements

- Python 3.6 or higher
- `pywinauto`
- `pyperclip`

## Install

1. Clone the repository:

   ```bash
   git clone https://github.com/TacticalAxis/python-icloud-password-extractor.git
   ```

2. Install the required libraries (preferably in a virtual environment)

   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

1. Open iCloud on Windows

2. Enable Passwords and Keychain if not already enabled

3. Click "View in iCloud Passwords App"

4. Run the script:

   ```bash
   python3 extract_passwords.py
   ```

5. To convert the extracted data to a specific format, run one of the following commands:

   - For Bitwarden format:

     ```bash
     python3 convert_to_bitwarden.py
     ```

   - For Proton Pass format:

     ```bash
     python3 convert_to_protonpass.py
     ```


## Output

The output JSON file will contain a list of password entries with fields for username, password, and website.

## Important Notes

- **Security**: This script reads sensitive information. Ensure it is used in a secure and ethical manner, compliant with privacy laws and regulations.
- **Compatibility**: Designed to work with Windows applications. For other operating systems, the script will require modifications.

## Contribution

Contributions are welcome. Please fork the repository and submit pull requests with your suggested changes.
