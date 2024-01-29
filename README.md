# JSON Data Transformer: An ETL Project

## Overview
JSON Data Transformer is a Python-based ETL (Extract, Transform, Load) utility designed to transform the structure of JSON data. It is particularly useful for renaming keys according to a predefined mapping. The project was initially created to process membership form data, converting it from an old format to a new one that is more suitable for further processing or storage.

## ETL Process
This project implements a simple ETL process:

1. **Extract**: Reads the original JSON data from an input file.
2. **Transform**: Applies a mapping to rename keys and restructure the data.
3. **Load**: Outputs the transformed data to a new JSON file.

## Features
- Load JSON data from a file
- Define key mappings for renaming
- Handle nested dictionaries
- Transform data according to the mappings
- Write the transformed data to a new JSON file

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
