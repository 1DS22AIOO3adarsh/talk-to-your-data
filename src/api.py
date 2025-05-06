import os
from fastapi import FastAPI, UploadFile, File, Form
from src.query_engine import query_data

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), query: str = Form(...)):
    """Handles file upload and allows users to send custom queries."""
    
    file_path = os.path.join("data", file.filename)  # Save file in 'data' folder

    # Ensure 'data' folder exists
    os.makedirs("data", exist_ok=True)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Pass the directory instead of file path
    folder_path = os.path.dirname(file_path)  

    # Query Gemini using user-provided query
    response = query_data(folder_path, query)

    return {"response": response}
