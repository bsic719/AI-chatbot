import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_functions import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
     print("Hello from ai-chatbot!")
     if api_key is None: 
          raise RuntimeError("GEMINI_API_KEY not found in environment")


     parser = argparse.ArgumentParser(description='Chatbot')
     parser.add_argument("user_prompt", type=str, help='User prompt, sent to Gemini')
     parser.add_argument("--verbose", action='store_true', help='Enable verbose output')
     # below accepts a second argument 
     # parser.add_argument("user_prompt2", type=str, help='User prompt, sent to Gemini')
     args = parser.parse_args()
     # print(args.user_prompt2)

     messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

     # original answer generated from calling Gemini-AI
     # answer = client.models.generate_content(model='gemini-2.5-flash', contents=messages)

     available_functions = types.Tool(
          function_declarations=[schema_get_files_info, schema_get_file_contents, schema_run_python_file, schema_write_file_contents]
     )

     answer = client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

     prompt_t_count = answer.usage_metadata.prompt_token_count
     candidates_t_count = answer.usage_metadata.candidates_token_count

     if args.verbose:
          if prompt_t_count is None:
               raise RuntimeError("Failed API request")
          print(f"User prompt: {args.user_prompt}")
          print(f"Prompt tokens: {prompt_t_count}")
          print(f"Response tokens: {candidates_t_count}")

     if answer.function_calls:
          for function in answer.function_calls:
               print(f"Calling function: {function.name}({function.args})")
     else:
          print(answer.text)



if __name__ == "__main__":
    main()