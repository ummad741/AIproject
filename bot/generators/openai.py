import openai
import os
from config import *

openai.api_key = OPENAI_API_KEY


with open("information.txt", "r") as file:
    file_data = file.read()

async def ask_gpt(question):
    prompt = f"The following information is extracted from the file:\n{file_data}\n\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=100, 
        temperature=0.7,
    )
    return response.choices[0].text.strip()


