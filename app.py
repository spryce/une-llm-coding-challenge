"""TODO: Add some docstring details."""

import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()  # Explicitly load .env file to avoid issues in production
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"
chat_session_histories = {}

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set!")

# Initialise Flask app
app = Flask(__name__)

# Configure Flask session storage
app.secret_key = os.getenv("FLASK_SECRET_KEY")

if not app.secret_key:
    raise ValueError("FLASK_SECRET_KEY is not set!")

app.config["SESSION_TYPE"] = "filesystem" # TODO: Change to Redis for production
Session(app)

# Initialize LangChain with OpenAI model
llm = ChatOpenAI(
    model=MODEL,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=openai_api_key,
)

llm_with_history = RunnableWithMessageHistory(
    llm,
    get_session_history=lambda session_id: chat_session_histories.setdefault(
        session_id, InMemoryChatMessageHistory()
    ),
)

@app.route("/", methods=["GET", "POST"])
def home():
    """Handles user queries and returns model responses."""
    if request.method == "POST":

        # Check Flask session for session ID or generate a new one
        if "session_id" not in session:
            session["session_id"] = str(uuid.uuid4())

        session_id = session["session_id"]
        config = {"configurable": {"session_id": session_id}}
        print("Session ID:", session_id)
        user_input = request.form["user_input"]
        print("User input:", user_input)
        messages = [("human", user_input)]
        print("Messages:", messages)
        ai_msg = llm_with_history.invoke(messages, config)
        print("AI response:", ai_msg.content)
        return jsonify({"response": ai_msg.content, "session_id": session_id})
    return render_template('index.html')

if __name__ == "__main__":
    # TODO Remove debug... Enable in .env
    app.run(debug=True)
