import os
from dotenv import load_dotenv
from groq import Groq

# Load the API key from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Store conversation history (limit to last 20 exchanges to manage tokens)
messages = []
MAX_HISTORY = 20

print("========================================")
print("        Groq AI Chatbot")
print("   Type 'quit' or 'exit' to stop")
print("========================================\n")

while True:
    try:
        # Get user input
        user_input = input("You: ").strip()

        # Exit condition
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        # Skip empty input
        if not user_input:
            continue

        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Keep history manageable
        if len(messages) > MAX_HISTORY:
            messages = messages[-MAX_HISTORY:]

        # Send message to Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,       # 0 = focused/deterministic, 1 = creative/random
            max_tokens=1024
        )

        # Extract the reply
        reply = response.choices[0].message.content

        # Add assistant reply to history (so it remembers context)
        messages.append({
            "role": "assistant",
            "content": reply
        })

        print(f"\nAI: {reply}\n")

    except Exception as e:
        print(f"\nError: {str(e)}\n")
        continue