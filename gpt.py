from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def chat_gpt(user_message):

    client = OpenAI(
        # This is the default and can be omitted
        api_key = os.getenv('OPENAI_API_KEY')
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a twitter social media manager for the travel agency 'Dube Travels'. All responses must be 200 characters or less ",
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Access the content using the 'message' attribute of the Choice object
    assistant_message = chat_completion.choices[0].message.content

    return assistant_message
