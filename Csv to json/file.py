import os
import csv
import json

print("CSV To JSON Converter....")

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    data = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    if not data:
        raise ValueError("CSV file is empty.")

    return data

def convert_csv_to_json(csv_data, output_file):
    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(csv_data, jsonfile, indent=4)

    print(f"Converted {len(csv_data)} records to '{output_file}'")

def main():
    try:
        csv_data = load_csv_data(INPUT_FILE)
        convert_csv_to_json(csv_data, OUTPUT_FILE)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

