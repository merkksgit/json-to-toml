#!/bin/bash

# Function to print usage instructions
print_usage() {
    echo "Usage: $0 <input_json_file> <output_toml_file>"
    exit 1
}

# Function to check if required commands exist
check_dependencies() {
    local missing_deps=()
    
    if ! command -v jq &> /dev/null; then
        missing_deps+=("jq")
    fi
    
    if ! command -v yq &> /dev/null; then
        missing_deps+=("yq")
    fi
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        echo "Error: Missing required dependencies: ${missing_deps[*]}"
        echo "Please install them using your package manager."
        echo "For example:"
        echo "  apt-get install jq yq    # For Debian/Ubuntu"
        echo "  brew install jq yq       # For macOS"
        exit 1
    fi
}

# Function to validate JSON file
validate_json() {
    local json_file="$1"
    if ! jq empty "$json_file" 2>/dev/null; then
        echo "Error: Invalid JSON format in '$json_file'"
        return 1
    fi
    return 0
}

# Function to convert JSON to TOML
json_to_toml() {
    local json_file="$1"
    local toml_file="$2"
    
    # Check if input file exists
    if [ ! -f "$json_file" ]; then
        echo "Error: Input file '$json_file' does not exist"
        return 1
    fi
    
    # Validate JSON format
    if ! validate_json "$json_file"; then
        return 1
    fi
    
    # Create output directory if it doesn't exist
    mkdir -p "$(dirname "$toml_file")"
    
    # Convert JSON to TOML using yq
    if ! yq -P '.' "$json_file" > "$toml_file" 2>/dev/null; then
        echo "Error converting to TOML"
        return 1
    fi
    
    echo "Successfully converted '$json_file' to '$toml_file'"
    return 0
}

# Main script

# Check if correct number of arguments provided
if [ $# -ne 2 ]; then
    print_usage
fi

# Check for required dependencies
check_dependencies

# Convert the file
if ! json_to_toml "$1" "$2"; then
    exit 1
fi

exit 0
