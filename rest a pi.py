import requests
import os

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = "gpt-4" # your model deployment name

url = f"{endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2024-02-01"

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how can you help me?"}
    ],
    "temperature": 0.7,
    "max_tokens": 800
}

response = requests.post(url, headers=headers, json=payload)
response_text = response.json()['choices'][0]['message']['content']
