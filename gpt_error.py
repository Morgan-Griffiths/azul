import sys
import openai
import io
import traceback
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# class GPTErrorStream(io.StringIO):
#     def __init__(self):
#         super().__init__()
#         self.buffer = ""

#     def writen(self, text):
#         self.buffer += text

#         # Check for a double newline, which may indicate the end of an error message
#         if self.buffer.endswith("\n\n"):
#             self.handle_error_message()
#     def write(self, text):
#         # response = openai.Completion.create(
#         #     engine="text-davinci-002",
#         #     prompt=f"Explain the following Python error message:\n{text}",
#         #     max_tokens=100,
#         #     n=1,
#         #     stop=None,
#         #     temperature=0.5,
#         # )
#         # print('response',response)

#         # gpt_output = response.choices[0].text.strip()
#         # sys.stdout.write(f"Original Error: {text}\nGPT Explanation: {gpt_output}\n")
#         sys.stdout.write(f"Original Error: {repr(text)}\n")
#         self.buffer = ""

response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a Python program that prints 'Hello, world!'",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

happy_dir = '/Users/Shuza/Code/sandbox/Dockerfile/happy'
with open(f'{happy_dir}/gpt_output.txt', 'w') as f:
    f.write(response.choices[0].text.strip())

# gpt_output = response.choices[0].text.strip()

# sys.stderr = GPTErrorStream()
# def gpt_excepthook(exc_type, exc_value, exc_traceback):
#     # Format the error message
#     error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    
#     # Process the error message using GPT
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=f"Explain the following Python error message:\n{error_message}",
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     gpt_output = response.choices[0].text.strip()

#     # Write the original error message and the GPT explanation to stdout
#     sys.stdout.write(f"Original Error: {error_message} GPT Explanation: {gpt_output}\n")

# # Set the custom excepthook
# sys.excepthook = gpt_excepthook

# # Test with an error
# x = undefined_variable