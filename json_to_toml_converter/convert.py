"""
A script to convert JSON files to TOML format.

This module provides functionality to read JSON files and convert their contents
to TOML format, saving the result to a new file.
"""

import json
import sys
from pathlib import Path

import toml


def json_to_toml(json_file: str, toml_file: str) -> bool:
    """
    Convert a JSON file to TOML format and save it to a new file.

    Args:
        json_file (str): Path to the input JSON file
        toml_file (str): Path to the output TOML file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Validate input file exists
        if not Path(json_file).is_file():
            print(f"Error: Input file '{json_file}' does not exist")
            return False

        # Read the JSON file
        with open(json_file, "r", encoding="utf-8") as jf:
            try:
                json_data = json.load(jf)
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON format in '{json_file}': {str(e)}")
                return False

        # Convert JSON data to TOML format
        toml_data = toml.dumps(json_data)

        # Ensure output directory exists
        output_path = Path(toml_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save the TOML data to a file
        with open(toml_file, "w", encoding="utf-8") as tf:
            tf.write(toml_data)

        print(f"Successfully converted '{json_file}' to '{toml_file}'")
        return True

    except (IOError, PermissionError) as e:
        print(f"Error accessing files: {str(e)}")
        return False
    except toml.TomlDecodeError as e:
        print(f"Error converting to TOML: {str(e)}")
        return False


def main():
    """Handle command line interface and argument validation."""
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_json_file> <output_toml_file>")
        sys.exit(1)

    success = json_to_toml(sys.argv[1], sys.argv[2])
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
