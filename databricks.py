import os
import openai

# Set environment variables
os.environ['AZURE_OPENAI_KEY'] = 'jdfdjfdfdjfj'
os.environ['AZURE_OPENAI_ENDPOINT'] = 'https://openai-gpt4o-demo.openai.azure.com/'

# Initialize Azure OpenAI configuration
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2024-02-15-preview"

def chat_with_gpt4(prompt):
    try:
        response = openai.ChatCompletion.create(
            engine="gpt-4o",  # Use your deployed model name or engine name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Chat with GPT-4 (type 'quit' to exit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
            
        response = chat_with_gpt4(user_input)
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    main()
