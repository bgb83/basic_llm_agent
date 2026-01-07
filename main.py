import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from schema_declarations import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = 'gemini-2.5-flash' 
function_map = {
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
    "get_files_info": get_files_info,
 }
limit = 20

def call_function(function_call, verbose=False):
    function_name = function_call.name or ""
    args = dict(function_call.args) if function_call.args else {}
    args['working_directory'] = "calculator"
    if verbose: 
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")
    if function_name == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    else:
        function_result = function_map[function_name](**args)
        print(function_result)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )

def main():
    messages = []
    print("Hello from basic-llm-agent!")
    try: 
        user_prompt = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file, ])
        counter = 0
        verbose=False
        for counter in range(limit):
            response = client.models.generate_content(
                model=model,
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
            )
            metadata = response.usage_metadata
            if len(sys.argv) == 3 and sys.argv[2] == '--verbose': 
                verbose = True
                print(f'User prompt: {user_prompt}')
                print(f'Prompt tokens: {metadata.prompt_token_count}')
                print(f'Response tokens: {metadata.candidates_token_count}')
            if len(response.candidates) > 0:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            function_responses = []
            if response.function_calls is None:
                break
            else:
                for function_call in response.function_calls:
                    function_call_result = call_function(function_call,verbose)
                    print(function_call_result.parts[0].function_response.response)
                    if len(function_call_result.parts) == 0:
                        raise Exception('empty parts')
                    if function_call_result.parts[0].function_response is None:
                        raise Exception('empty response')
                    if function_call_result.parts[0].function_response.response is None:
                        raise Exception('no response')
                    function_responses.append(function_call_result.parts[0])
                    # if verbose:
                    #     print(f"-> {function_call_result.parts[0].function_response.response}")
                messages.append(types.Content(role="user", parts=function_responses))
        if counter == limit - 1:
            print(f'Sorry, I reached iteration limit of {counter}')
            sys.exit(1)
        print(response.text)
    except IndexError:
        print('Sorry, I did not understand your request or you forgot to input it!')
        sys.exit(1)

if __name__ == "__main__":
    main()
