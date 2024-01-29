import json

# Define the path for the input and output JSON files
INPUT_FILE_PATH = r"PATH_TO_YOUR_INPUT_FILE"
OUTPUT_FILE_PATH = r'PATH_TO_YOUR_OUTPUT_FILE'

# Load JSON data from the input file
with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to extract and rename keys based on the provided mapping
def extract_and_rename_keys(source, mapping):
    result = {}
    for old_key, new_key in mapping.items():
        if isinstance(new_key, dict):
            # For nested dictionaries, recurse
            result.update(extract_and_rename_keys(source.get(old_key, {}), new_key))
        else:
            # Directly assign the new key from the source
            result[new_key] = source.get(old_key) if source.get(old_key) else None
    return result

# Define key mappings for renaming
key_mapping = {
    "names": {
        "first_name": "FirstName",
        "last_name": "LastName"
    },
    "email": "EmailAddress",
    "phone": "PhoneNumber",
    "address_1": {
        "address_line_1": "AddressLine1",
        "address_line_2": "AddressLine2",
        "city": "City",
        "state": "State",
        "zip": "ZipCode",
        "country": "Country"
    },
    "input_text_4": "NameForSignature",
    "datetime": "DateOfSignature",
    "description": "Comments"
}

# Process each entry in the data
new_data = [extract_and_rename_keys(entry.get('response', {}), key_mapping) for entry in data]

# Write the transformed data to the output file
with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(new_data, file, indent=4)

print("Data Transformed")
