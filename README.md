# JSON to TOML Converter

A simple command-line tool that converts JSON files into TOML format.

## Overview

This project provides a straightforward way to convert JSON files to TOML format using a command-line interface. It's designed to be simple and efficient, making it easy to integrate into scripts or use manually.

## Requirements

- Python 3.x
- Required libraries:
  - `json` (built-in)
  - `toml`

## Installation

1. Clone the repository:

```bash
git clone git@github.com:merkksgit/json-to-toml.git
cd json_to_toml_converter
```

2. Ensure Python 3.x is installed:

```bash
python3 --version
```

If Python is not installed, you can install it:

```bash
sudo apt install python3
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

To convert a JSON file to TOML format, use the following command:

```bash
python3 convert.py <input_json_file> <output_toml_file>
```

For example:

```bash
python3 convert.py input.json output.toml
```

## Project Structure

```
json_to_toml_converter/
|-- convert.py       # Main conversion script
|-- requirements.txt # List of required libraries
|-- README.md       # Project documentation
```

## Error Handling

The script will display an error message if:

- Incorrect number of command-line arguments are provided
- Input file cannot be read
- Output file cannot be written
- JSON parsing fails

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

[MIT License](https://mit-license.org/)
