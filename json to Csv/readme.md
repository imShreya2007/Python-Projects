# JSON to CSV Converter (Python Console Application)

A **Python-based JSON to CSV Converter** that reads structured JSON data from a file and converts it into a CSV format.  
The program supports **API-style JSON responses**, performs validation, and handles errors gracefully to ensure reliable data transformation.

---

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Input & Output](#input--output)
- [Error Handling](#error-handling)
- [Concepts Covered](#concepts-covered)

---

## Features

- Converts JSON data into CSV format
- Supports:
  - Plain JSON arrays
  - API-style JSON responses with a `data` key
- Automatically extracts CSV headers from JSON keys
- Validates:
  - File existence
  - JSON format
  - Data structure
- Handles empty or invalid JSON safely
- Clean and minimal console output
- Uses only standard Python libraries

---

## Usage

1. Place your JSON file in the project directory  
   (Default file name: `api_data.json`)

2. Run the program:
```bash
python json_to_csv.py
```
3. The converted CSV file will be generated as:
```
converted_data.csv
```

---

## How It Works
1. Checks whether the input JSON file exists
2. Loads and parses the JSON content
3. Detects API-style JSON ({ "data": [...] }) automatically
4. Validates that the JSON contains a non-empty list of objects
5. Collects all unique keys across records to form CSV headers
6. Writes structured data into a CSV file
7. Displays a success message with the number of records converted

---

## Input & Output
Example JSON Input
```
{
  "data": [
    { "id": 1, "name": "Alice", "age": 22 },
    { "id": 2, "name": "Bob", "age": 25 }
  ]
}
```
```
Example CSV Output
id,name,age
1,Alice,22
2,Bob,25
```

---

## Error Handling
The program safely handles:
* Missing input files
* Invalid JSON formatting
* Incorrect JSON structure
* Empty data sets
Clear error messages are displayed without crashing the program.

---

## Concepts Covered
* File handling (JSON & CSV)
* Data serialization and parsing
* Dictionary and list processing
* Dynamic CSV header generation
* Exception handling
* Modular function-based design
* Console-based automation scripts

---
