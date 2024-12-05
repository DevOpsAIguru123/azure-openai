from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

# Get service credentials
credential = dbutils.credentials.getServiceCredentialsProvider("svc-cred-nprd-openai")

# Get bearer token provider
def get_bearer_token_provider():
    return credential.token

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="https://opena.openai.azure.com/",
    api_version="2024-02-15-preview",
    azure_ad_token_provider=get_bearer_token_provider
)

# Test with a simple chat completion
response = client.chat.completions.create(
    model="gpt-4o",  # Replace with your actual deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print response
print(response.choices[0].message.content)


