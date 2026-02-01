import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import *
from call_functions import *
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
     if api_key is None: 
          raise RuntimeError("GEMINI_API_KEY not found in environment")

     # handles command-line arguments and parse it out to be used at variables 
     parser = argparse.ArgumentParser(description='Chatbot')
     parser.add_argument('user_prompt', type=str, help='User prompt')
     parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
     args = parser.parse_args()
     
     messages = [types.Content(role='user', parts=[types.Part(text=args.user_prompt)])]

     for _ in range(20): 
          ai_response = client.models.generate_content(
               model='gemini-2.5-flash', 
               contents=messages,
               config = types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=1.0,
                    tools=[available_functions],
                    ),
               )

          # adding AI's response to messages for history
          if ai_response.candidates:
               for response in ai_response.candidates:
                    messages.append(response.content)


          if ai_response.usage_metadata == None:
               raise RuntimeError('No usage metadata returned; request may have failed')
          prompt_token_ct = ai_response.usage_metadata.prompt_token_count
          response_token_ct = ai_response.usage_metadata.candidates_token_count

          function_responses = []
          # if args.verbose:
          #      print(f"User prompt: {args.user_prompt}")
          #      print(f"Prompt tokens: {prompt_token_ct}")
          #      print(f"Response tokens: {response_token_ct}")

          print('\nResponse:')
          if ai_response.function_calls == None:
               print(ai_response.text)
               break
          else:
               for function in ai_response.function_calls:
                    if args.verbose:
                         function_call_result = call_function(function, args.verbose)
                    else:
                         function_call_result = call_function(function)

                    if not function_call_result.parts:
                         raise Exception
                    if function_call_result.parts[0].function_response == None:
                         raise Exception
                    if function_call_result.parts[0].function_response.response == None:
                         raise Exception

                    function_responses.append(function_call_result.parts[0])
                    if args.verbose:
                         print(f"-> {function_call_result.parts[0].function_response.response}")
          
          # 
          messages.append(types.Content(role='user', parts=function_responses))
          if _ == 20:
               sys.exit(1)

if __name__ == "__main__":
    main()