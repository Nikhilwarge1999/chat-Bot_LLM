import os
import requests
from dotenv import load_dotenv

load_dotenv()

def call_groq_gpt(prompt, model="llama3-70b-8192"):
    api_key = os.getenv("GROQ_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful medical diagnosis assistant. Ask follow-up questions if needed."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
    return response.json()['choices'][0]['message']['content']
