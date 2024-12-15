# JSON to TOML Converter

A simple command-line tool that converts JSON files into TOML format, available in both Python and Bash implementations.

## Overview

This project provides straightforward ways to convert JSON files to TOML format using command-line interfaces. It's designed to be simple and efficient, making it easy to integrate into scripts or use manually.

## Python Implementation

### Requirements

- Python 3.x
- Required libraries:
  - `json` (built-in)
  - `toml`

### Installation

1. Clone the repository:

```bash
git clone git@github.com:merkksgit/json-to-toml.git
cd json_to_toml_converter
```

2. Ensure Python 3.x is installed:

```bash
python3 --version
```

If Python is not installed:

```bash
sudo apt install python3
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

### Usage

```bash
python3 convert.py <input_json_file> <output_toml_file>
```

Example:

```bash
python3 convert.py input.json output.toml
```

## License

[MIT License](https://mit-license.org/)
