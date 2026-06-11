from langfuse import Langfuse
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# =========================
# Langfuse
# =========================

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_BASE_URL")
)

print("Langfuse Connected:", langfuse.auth_check())

# =========================
# Gemini
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("me_key"),
    temperature=0.4
)

# =========================
# Prompt
# =========================

question = input("Enter your question: ")

# =========================
# Create Trace
# =========================

trace = langfuse.trace(
    name="mental-health-chatbot",
    input=question
)

try:

    response = llm.invoke(question)

    answer = response.content

    print("\nResponse:\n")
    print(answer)

    trace.update(
        output=answer
    )

except Exception as e:

    print("\nError:")
    print(str(e))

    trace.update(
        output=f"ERROR: {str(e)}"
    )

# =========================
# Send Trace
# =========================

langfuse.flush()

print("\nTrace Sent Successfully")