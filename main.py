import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = 'gemini-2.5-flash'

def main():
    print("Hello from basic-llm-agent!")
    try: 
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        response = client.models.generate_content(
            model=model,
            contents=messages,
        )
        metadata = response.usage_metadata
        print(response.text)
        if len(sys.argv) == 3 and sys.argv[2] == '--verbose': 
            print(f'User prompt: {user_prompt}')
            print(f'Prompt tokens: {metadata.prompt_token_count}')
            print(f'Response tokens: {metadata.candidates_token_count}')
    except IndexError:
        print('Sorry, I did not understand your request or you forgot to input it!')
        sys.exit(1)

if __name__ == "__main__":
    main()
