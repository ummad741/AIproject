from openai import AsyncClient, AsyncOpenAI,OpenAI
# local files
from bot.config import OPENAI_API_KEY,AI_BASE_URL


client = AsyncOpenAI(
    api_key = OPENAI_API_KEY,
    base_url = AI_BASE_URL
)

async def chat_gpt(request):
    response =  await client.chat.completions.create(
        model="gpt-4o",
        messages= [
            {
                "role":"user",
                "content": request 
            }
        ]
    )
    print(response)

    return response.choices[0].message.content


# with open("information.txt", "r") as file:
#     file_data = file.read()

# async def ask_gpt(question):
#     prompt = f"The following information is extracted from the file:\n{file_data}\n\nQuestion: {question}\nAnswer:"
#     response = openai.Completion.create(
#         engine="text-davinci-003",  
#         prompt=prompt,
#         max_tokens=100, 
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

