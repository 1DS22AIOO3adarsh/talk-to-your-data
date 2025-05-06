import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System Prompt to enforce structured output
SYSTEM_PROMPT = """You are an AI assistant specialized in data analysis, capable of processing various file types including PDF, CSV, and JSON. 
When given a dataset (or file) and a query, provide a concise and structured answer within 4-5 lines. 
Structure your response to include: 
1. A brief identification of the data source (e.g., "From the provided CSV file...", "Based on the extracted text from the PDF...").
2. The core answer to the query, presented clearly and directly.
3. Relevant numerical results or extracted text, as required by the query.
4. If applicable, a brief note about the data's context or limitations.

STRICT OUTPUT RULES:
1. If the query requires numerical computation, return the final computed result within the structured response.
2. If text extraction is needed, return the relevant text within the structured response.
3. Avoid unnecessary explanations or assumptions.
"""

def query_gemini(user_prompt):
    """Queries Gemini with a strict system instruction to return only structured results."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{SYSTEM_PROMPT}\n\nUser Query: {user_prompt}")
    return response.text.strip()  # Ensure clean output
