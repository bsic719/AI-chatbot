import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
     print("Hello from ai-chatbot!")
     if api_key is None: 
          raise RuntimeError("GEMINI_API_KEY not found in environment")

     # model = 'gemini-2.5-flash'
     # contents = 'what is 1 + 1'
     # answer = client.models.generate_content(model = 'gemini-2.5-flash', contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
     answer = client.models.generate_content(model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

)
     prompt_t_count = answer.usage_metadata.prompt_token_count
     candidates_t_count = answer.usage_metadata.candidates_token_count

     if prompt_t_count is None:
          raise RuntimeError("Failed API request")
     print(f"Prompt tokens: {prompt_t_count}")
     print(f"Response tokens: {candidates_t_count}")

     print(answer.text)


    


if __name__ == "__main__":
    main()