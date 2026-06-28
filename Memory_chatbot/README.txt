Memory-Based AI Chatbot
=======================

A conversational AI chatbot built with Streamlit that remembers previous messages
within a session using memory storage.


FEATURES
--------
- Chat with an AI assistant powered by Groq
- Remembers conversation history (memory-based context)
- Simple and clean Streamlit UI
- Fast responses using Groq's LLM API


TECH STACK
----------
- Python
- Streamlit       (UI)
- Groq API        (LLM)
- ChromaDB        (Vector memory storage)
- python-dotenv   (Environment variables)


PROJECT STRUCTURE
-----------------
memory-chatbot/
├── app.py              # Main Streamlit app
├── chatbot.py          # Groq AI logic
├── memory.py           # Memory/history management
├── requirements.txt    # Dependencies
├── .env                # API keys (do NOT share)
├── .gitignore
└── README.txt


SETUP INSTRUCTIONS
------------------

1. Clone the repository
   git clone https://github.com/CrwazzyCupcakes/Gen-ai-Workshop-CBIT_Edspark.git
   cd Gen-ai-Workshop-CBIT_Edspark/Memory_chatbot

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   Create a .env file in the root folder:
   GROQ_API_KEY=your_groq_api_key_here

   Get your free API key at: https://console.groq.com

5. Run the app
   streamlit run app.py

6. Open your browser
   Go to: http://localhost:8501


USAGE
-----
- Type a message in the input box and press Enter
- The chatbot will respond based on your message and conversation history
- The memory resets when you refresh the page


AUTHOR
------
Mohammed Afnan
Gen-AI Internship Project
