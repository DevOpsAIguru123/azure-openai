import requests
import json

# Databricks service credential setup
token_provider = dbutils.credentials.getServiceCredentialProvider("openai-service-credential")

# Azure OpenAI details
endpoint = "https://<your-openai-resource-name>.openai.azure.com/"
deployment_name = "gpt-4-deployment"
api_version = "2024-04-01-preview"

# Construct headers
headers = {
    "Authorization": f"Bearer {token_provider.getAccessToken()}",
    "Content-Type": "application/json"
}

# GPT-4 prompt payload
payload = {
    "messages": [
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
}

# Send request to Azure OpenAI
response = requests.post(
    f"{endpoint}openai/deployments/{deployment_name}/chat/completions?api-version={api_version}",
    headers=headers,
    json=payload
)

# Print response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")