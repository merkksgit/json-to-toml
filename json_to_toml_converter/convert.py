# Import necessary libraries
import json
import toml
import sys

def json_to_toml(json_file, toml_file):
    # Read the JSON file
    with open(json_file, 'r') as jf:
        json_data = json.load(jf)

    # Convert JSON data to TOML format
    toml_data = toml.dumps(json_data)

    # Save the TOML data to a file
    with open(toml_file, 'w') as tf:
        tf.write(toml_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_json_file> <output_toml_file>")
        sys.exit(1)
    json_to_toml(sys.argv[1], sys.argv[2])