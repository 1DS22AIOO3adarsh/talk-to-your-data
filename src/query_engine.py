import os
from models.gemini_llm import query_gemini
from src.data_loader import load_data_from_folder

def query_data(folder_path, user_query):
    """Load all file data from a folder and query Gemini for insights."""
    
    # If given a file, extract its directory
    if os.path.isfile(folder_path):
        folder_path = os.path.dirname(folder_path)  # Extract folder path
    
    # Ensure it's a valid directory
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Invalid directory: {folder_path}")

    # Load all files in the folder
    data = load_data_from_folder(folder_path)

    # Convert data to a string (limit to avoid excessive token usage)
    data_str = str(data)
    if len(data_str) > 5000:
        data_str = data_str[:5000] + "...\n[Data Truncated]"

    prompt = f"Here is some data:\n\n{data_str}\n\nUser query: {user_query}\n\nProvide a detailed response."
    response = query_gemini(prompt)
    return response
