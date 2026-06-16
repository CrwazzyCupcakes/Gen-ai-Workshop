import streamlit as st

from memory import save_memory
from memory import retrieve_memory
from chatbot import ask_bot

st.set_page_config(
    page_title="Memory AI",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #111827
    );
}

.main-title {
    text-align:center;
    font-size:55px;
    font-weight:700;
    color:white;
}

.sub-title {
    text-align:center;
    color:#94a3b8;
    margin-bottom:30px;
}

.response-box {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    color:white;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🧠 Memory AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Your Personal Memory Based Chatbot</div>',
    unsafe_allow_html=True
)

user_input = st.text_input(
    "",
    placeholder="Ask me anything..."
)

if user_input:

    memories = retrieve_memory(user_input)

    response = ask_bot(
        user_input,
        memories
    )

    st.markdown(
        f"""
        <div class="response-box">
        {response}
        </div>
        """,
        unsafe_allow_html=True
    )

    important_patterns = [
        "i am",
        "my name is",
        "i like",
        "i love",
        "i use",
        "my favorite"
    ]

    if any(
        p in user_input.lower()
        for p in important_patterns
    ):
        save_memory(user_input)