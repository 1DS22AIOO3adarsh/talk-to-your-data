import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload/"  # FastAPI backend URL

st.title("Talk to Your Data")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "json", "txt"])

query = st.text_area("Enter your query", "Calculate the mean of all numerical columns.")

if uploaded_file and query:
    if st.button("Ask AI"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        data = {"query": query}

        response = requests.post(API_URL, files=files, data=data)

        if response.status_code == 200:
            st.success("Response:")
            
            st.write(response.json()["response"])  # Original line causing error

        else:
            st.error("Error in response. Check API logs.")
