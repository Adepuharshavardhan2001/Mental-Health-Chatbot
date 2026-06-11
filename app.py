import streamlit as st
import os
import logging
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =====================================
# Load Environment Variables
# =====================================

load_dotenv()

# =====================================
# Logging
# =====================================

logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================================
# API Key
# =====================================

api_key = os.getenv("me_key")

if not api_key:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

# =====================================
# Streamlit Config
# =====================================

st.set_page_config(
    page_title="CalmMind",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 CalmMind")
st.caption("Mental Health Support Assistant")

# =====================================
# Gemini Model
# =====================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.4
)

# =====================================
# Prompt Template
# =====================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are CalmMind, an empathetic Mental Health Support Assistant.

Your role:
1. Identify the user's emotion.
2. Provide emotional support.
3. Suggest practical coping strategies.
4. End with encouragement.

Rules:
- Do not diagnose illnesses.
- Do not prescribe medication.
- Do not claim to be a therapist.
- Encourage professional help when appropriate.

Response Format:

### Emotion
<emotion>

### Support
<support>

### Suggestions
- suggestion 1
- suggestion 2
- suggestion 3

### Encouragement
<encouragement>
"""
        ),
        ("human", "{question}")
    ]
)

# =====================================
# Chain
# =====================================

chain = prompt | llm | StrOutputParser()

# =====================================
# Crisis Detection
# =====================================

HIGH_RISK_KEYWORDS = [
    "suicide",
    "kill myself",
    "self harm",
    "end my life"
]

def crisis_detected(text):
    text = text.lower()
    return any(keyword in text for keyword in HIGH_RISK_KEYWORDS)

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================
# Display Previous Messages
# =====================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# User Input
# =====================================

user_input = st.chat_input("How are you feeling today?")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                if crisis_detected(user_input):

                    response = """
⚠️ I'm concerned about your safety.

Please contact:
• A trusted family member
• A close friend
• A mental health professional
• Local emergency services

You do not need to face this alone.
"""

                else:

                    response = chain.invoke(
                        {
                            "question": user_input
                        }
                    )

                st.markdown(response)

                logging.info(f"User: {user_input}")
                logging.info(f"Assistant: {response}")

            except Exception as e:

                error_message = str(e)

                logging.error(error_message)

                st.error("Actual Error:")
                st.code(error_message)

                response = f"Error: {error_message}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.header("About CalmMind")

    st.write("""
• Emotional support

• Stress management

• Mindfulness guidance

• Positive coping strategies
""")

    st.divider()

    st.subheader("Suggested Questions")

    st.write("• I feel stressed about exams")
    st.write("• I feel anxious before interviews")
    st.write("• How can I stop overthinking?")
    st.write("• How do I improve my confidence?")

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()