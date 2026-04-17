import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔹 Load environment variables
load_dotenv()

# 🔹 Get API key
api_key = os.getenv("OPENAI_API_KEY")

# 🔹 Initialize client
client = OpenAI(api_key=api_key)


# 🔹 Generate Summary (Mock version to avoid quota error)
def generate_summary(description):
    return f"This is a summary of the book: {description[:50]}..."


# 🔹 Q&A (Mock version to avoid quota error)
def ask_question(context, question):
    return f"Based on available books, the answer to '{question}' is related to stored descriptions."