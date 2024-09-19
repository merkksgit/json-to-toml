import tkinter as tk
from tkinter import filedialog, messagebox
import json
import toml

def json_to_toml(json_file, toml_file):
    try:
        # Read the JSON file
        with open(json_file, 'r') as jf:
            json_data = json.load(jf)

        # Convert JSON data to TOML format
        toml_data = toml.dumps(json_data)

        # Save the TOML data to a file
        with open(toml_file, 'w') as tf:
            tf.write(toml_data)

        return True, "Conversion successful!"
    except Exception as e:
        return False, f"Error during conversion: {str(e)}"

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON to TOML Converter")
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the file inputs
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Input JSON file label and button
        self.json_label = tk.Label(frame, text="Select JSON File:")
        self.json_label.grid(row=0, column=0, padx=5, pady=5)

        self.json_entry = tk.Entry(frame, width=40)
        self.json_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_json_button = tk.Button(frame, text="Browse", command=self.browse_json)
        self.browse_json_button.grid(row=0, column=2, padx=5, pady=5)

        # Output TOML file label and button
        self.toml_label = tk.Label(frame, text="Save TOML As:")
        self.toml_label.grid(row=1, column=0, padx=5, pady=5)

        self.toml_entry = tk.Entry(frame, width=40)
        self.toml_entry.grid(row=1, column=1, padx=5, pady=5)

        self.browse_toml_button = tk.Button(frame, text="Browse", command=self.save_toml)
        self.browse_toml_button.grid(row=1, column=2, padx=5, pady=5)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack(pady=5)

    def browse_json(self):
        # Open a file dialog to select JSON file
        json_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if json_file:
            self.json_entry.delete(0, tk.END)
            self.json_entry.insert(0, json_file)

    def save_toml(self):
        # Open a file dialog to save the TOML file
        toml_file = filedialog.asksaveasfilename(defaultextension=".toml", filetypes=[("TOML files", "*.toml")])
        if toml_file:
            self.toml_entry.delete(0, tk.END)
            self.toml_entry.insert(0, toml_file)

    def convert(self):
        # Get file paths from input fields
        json_file = self.json_entry.get()
        toml_file = self.toml_entry.get()

        if not json_file or not toml_file:
            messagebox.showwarning("Missing Files", "Please select both input JSON and output TOML files.")
            return

        # Perform the conversion
        success, message = json_to_toml(json_file, toml_file)
        if success:
            self.status_label.config(text=message, fg="green")
        else:
            self.status_label.config(text=message, fg="red")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
