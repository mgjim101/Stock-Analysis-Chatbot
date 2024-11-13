import openai

openai.api_key = "Add APK_KEY here"

try:
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Use the supported model
        prompt="Say hello!",
        max_tokens=5
    )
    print(response)
except Exception as e:
    print(f"Error: {e}")
