"""TODO: Add some docstring details."""

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()  # Explicitly load .env file to avoid issues in production
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"
SESSION_ID = "sdfsdfsdf"
store = {} # simple conversation store for multiple sessions

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set!")

# Initialise Flask app
app = Flask(__name__)

# Initialize LangChain with OpenAI model
llm = ChatOpenAI(
    model=MODEL,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=openai_api_key,
)

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """Return the chat history for the given session_id."""
    # print("Session ID:", session_id)
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

llm_with_history = RunnableWithMessageHistory(llm, get_session_history)

config = {"configurable": {"session_id": SESSION_ID}}


@app.route("/", methods=["GET", "POST"])
def home():
    """Handles user queries and returns model responses."""
    if request.method == "POST":
        user_input = request.form["user_input"]
        print("User input:", user_input)
        messages = [("human", user_input)]
        print("Messages:", messages)
        ai_msg = llm_with_history.invoke(messages, config)
        print("AI response:", ai_msg.content)
        return jsonify({"response": ai_msg.content})
    return render_template('index.html')

if __name__ == "__main__":
    # TODO Remove debug... Enable in .env
    app.run(debug=True)
