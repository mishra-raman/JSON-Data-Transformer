# JSON Data Transformer

## Overview
JSON Data Transformer is a Python-based utility designed to transform the structure of JSON data. It is particularly useful for renaming keys according to a predefined mapping. The project was initially created to process membership form data, converting it from an old format to a new one that is more suitable for further analysis, processing and storage.

## Features
- Load JSON data from a file
- Define key mappings for renaming
- Handle nested dictionaries
- Transform data according to the mappings
- Write the transformed data to a new JSON file

## How It Works
1. **Load Data**: Reads the original JSON data from an input file.
2. **Define Key Mappings**: Specifies how the old keys should be renamed to new keys, including handling nested dictionaries.
3. **Transform Data**: Iterates over each entry in the original data, applying the key mappings to rename keys and restructure the data.
4. **Write Data**: Outputs the transformed data to a new JSON file.

## Key Functions
- `extract_and_rename_keys(source, mapping)`: Recursively processes each key-value pair in the source data according to the mapping rules.

## Usage
To use the script, ensure that the input and output file paths are correctly set to the desired file locations. Then, simply run the script with Python, and it will generate the new JSON file with the transformed data structure.

## Requirements
- Python 3.x
- JSON data file to transform

## Input/Output
- Input: A JSON file with the original data structure.
- Output: A JSON file with the transformed data structure.

## Customization
To adapt the script to different data structures or requirements, modify the `key_mapping` dictionary to reflect the desired key transformations.
