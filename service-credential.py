from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

# Get service credentials from Unity Catalog
credentials = dbutils.credentials.getServiceCredentialsProvider('your-service-credential')

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint="https://{your-endpoint}.openai.azure.com/",
    api_version="2024-02-15-preview",
    azure_ad_token_provider=credentials
)[1][2]

# Example usage
response = client.chat.completions.create(
    model="your-deployment-name",
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)[3]
