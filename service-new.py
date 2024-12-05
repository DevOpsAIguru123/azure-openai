from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

# Get service credentials
credential = dbutils.credentials.getServiceCredentialsProvider("openai-access")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="https://your-resource-name.openai.azure.com",
    api_version="2024-02-01",
    credential=credential
)

# Create a simple chat completion
response = client.chat.completions.create(
    model="your-deployment-name",  # your GPT-4 deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print response
print(response.choices[0].message.content)
