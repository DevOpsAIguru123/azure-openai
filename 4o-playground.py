import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")

client.create_endpoint(
    name="azure-openai-gpt4o-playground",
    config={
        "served_entities": [{
            "name": "azure-openai-completions",
            "external_model": {
                "name": "gpt-4o",
                "provider": "openai",
                "task": "llm/v1/completions",
                "openai_config": {
                    "openai_api_type": "azure",
                    "openai_api_key": "key",
                    "openai_api_base": "https://your-azure-openai-endpoint.openai.azure.com",
                    "openai_deployment_name": "gpt-4o"
                }
            }
        }]
    }
)
