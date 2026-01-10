# list_gemini_models.py
# A simple script to list available Gemini models using the Google Gen AI SDK.

import os
from google.genai import Client

# Get your API key from: https://aistudio.google.com/app/apikey
# It's recommended to set it as an environment variable for security.
API_KEY = os.getenv("GEMINI_API_KEY", 'AIzaSyCx2Ui4Q9bqlURVhbZxcEFyWDU_iDtY92Y')  # or "GOOGLE_API_KEY"

if not API_KEY:
    raise ValueError("Please set your Gemini API key in the environment variable GEMINI_API_KEY "
                     "or GOOGLE_API_KEY, or hardcode it here (not recommended for production).")

# Create the client (uses the Gemini Developer API by default)
client = Client(api_key=API_KEY)

print("Available Gemini models:\n")
print("-" * 60)

# List all models (paginated iterator)
for model in client.models.list():
    name = model.name  # e.g., "models/gemini-2.5-flash"
    display_name = model.display_name or "N/A"
    description = model.description or "No description"
    # New attribute: supported_actions (list of strings like "generateContent", "embedContent")
    supported_actions = ", ".join(model.supported_actions) if model.supported_actions else "N/A"

    print(f"Name: {name}")
    print(f"Display Name: {display_name}")
    print(f"Description: {description}")
    print(f"Supported Actions: {supported_actions}")
    print("-" * 60)