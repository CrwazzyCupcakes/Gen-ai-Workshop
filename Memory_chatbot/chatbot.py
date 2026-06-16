from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)
def ask_bot(question, memories):

    memory_text = "\n".join(memories)

    prompt = f"""
You are a memory-based chatbot.

Relevant user memories:
{memory_text}

User question:
{question}

Use memories if useful.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content