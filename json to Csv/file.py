import json
import csv
import os

print("JSON To CSV Converter....")

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"


def load_json_data_from_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    with open(filename, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")


def convert_json_to_csv(json_data, output_file):
    # Handle API-style response
    if isinstance(json_data, dict) and "data" in json_data:
        json_data = json_data["data"]

    if not isinstance(json_data, list) or not json_data:
        raise ValueError("JSON data must be a non-empty list of objects.")

    fieldnames = set()
    for item in json_data:
        fieldnames.update(item.keys())

    fieldnames = list(fieldnames)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in json_data:
            writer.writerow(entry)

    print(f"Converted {len(json_data)} records to '{output_file}'")


def main():
    try:
        json_data = load_json_data_from_file(INPUT_FILE)
        convert_json_to_csv(json_data, OUTPUT_FILE)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
