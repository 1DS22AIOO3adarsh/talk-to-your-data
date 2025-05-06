import pandas as pd
import json
import os
from PyPDF2 import PdfReader

def load_pdf(file_path):
    """Reads text from a PDF file"""
    text = ""
    with open(file_path, "rb") as f:
        pdf = PdfReader(f)
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text if text else "Unable to extract text from PDF."

def load_csv(file_path):
    """Reads a CSV file and converts it to a string"""
    try:
        df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
        return df.to_string()
    except Exception as e:
        return f"Error reading CSV: {str(e)}"

def load_excel(file_path):
    """Reads an Excel file and converts it to a string"""
    try:
        df = pd.read_excel(file_path)
        return df.to_string()
    except Exception as e:
        return f"Error reading Excel: {str(e)}"

def load_json(file_path):
    """Reads a JSON file and converts it to a string"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return json.dumps(data, indent=4)
    except Exception as e:
        return f"Error reading JSON: {str(e)}"

def load_data_from_folder(folder_path):
    """Loads all files from the specified folder without printing output"""
    if not os.path.exists(folder_path):
        raise ValueError(f"Folder does not exist: {folder_path}")

    data = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            try:
                if file_name.endswith(".pdf"):
                    data[file_name] = load_pdf(file_path)
                elif file_name.endswith(".csv"):
                    data[file_name] = load_csv(file_path)
                elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
                    data[file_name] = load_excel(file_path)
                elif file_name.endswith(".json"):
                    data[file_name] = load_json(file_path)
                else:
                    data[file_name] = "Unsupported file format"
            except Exception as e:
                data[file_name] = f"Error processing file: {str(e)}"

    return data  # Only returns the loaded data, no prints

if __name__ == "__main__":
    # Specify the folder containing the data files
    data_folder = "C:/Users/adars/Desktop/End-to-end projects/talk-to-your-data/talk-to-your-data/data/"
    
    # Load all files silently
    loaded_data = load_data_from_folder(data_folder)
