# JSON to TOML Converter

This project allows you to convert JSON files into TOML format. You can use either the graphical user interface (GUI) for ease of use or stick to the command-line interface (CLI) for more control. Both methods achieve the same result: converting JSON files into TOML format and saving the output.

### Installation

Clone the repository:

```bash
git clone git@github.com:merkksgit/json-to-toml.git
cd json_to_toml_converter
```

Ensure Python 3.x is installed:

```bash
python3 --version
```
if not, run:

```bash
sudo apt install python3
```

Install required packages:

```bash
pip install -r requirements.txt
```

### Usage

Run `python3 convert.py input.json output.toml` to convert a JSON file to TOML format.

# JSON to TOML Converter with GUI

### Overview

This project provides a graphical user interface (GUI) for converting JSON files into TOML format. The GUI allows you to easily select JSON files, convert them, and save the results in TOML format without needing to use the command-line interface.

### Requirements

- Python 3.x
- Libraries: 
  - `json`
  - `toml`
  - `tkinter` (pre-installed with most Python distributions)


3. Ensure `tkinter` is installed:
    `tkinter` is usually installed by default with Python. However, in some environments, you may need to install it manually.

- **On Linux**:

    ```bash
    sudo apt-get install python3-tk
    ```

- **On macOS**:
    If `tkinter` is not working on macOS, you may need to reinstall Python using Homebrew:
    ```bash
    brew install python-tk
    ```

- **On Windows**:
    `tkinter` comes pre-installed with Python, so no additional installation should be required.

## Usage

### Running the GUI

1. To launch the GUI, run the following command:
    ```bash
    python3 gui_convert.py
    ```

2. **Using the GUI**:
    - **Select JSON File**: Click the "Browse" button and choose the JSON file you want to convert.
    - **Select TOML Output Location**: Click the "Browse" button and select the location to save the TOML file.
    - **Convert**: Click the "Convert" button to start the conversion process. A message will be displayed indicating whether the conversion was successful.

## Project Structure

json_to_toml_converter/  
|-- convert.py          # Script for CLI conversion  
|-- gui_convert.py    # Script for GUI conversion  
|-- requirements.txt    # List of required libraries  
|-- README.md           # Instructions and project documentation
