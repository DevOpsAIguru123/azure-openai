from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential

# Get service credentials properly
credential = dbutils.credentials.getServiceCredentialsProvider("svc-cred-nprd-openai")

# Initialize Azure OpenAI client correctly
client = AzureOpenAI(
    azure_endpoint="https://your-resource-name.openai.azure.com",
    api_version="2024-02-01",
    azure_ad_token_provider=credential
)

