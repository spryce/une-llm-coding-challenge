"""TODO: Add some docstring details."""

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from langchain_openai import ChatOpenAI

load_dotenv()  # Explicitly load .env file
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"

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

@app.route("/", methods=["GET", "POST"])
def home():
    """Handles user queries and returns model responses."""
    if request.method == "POST":
        user_input = request.form["user_input"]
        print("User input:", user_input)
        messages = [("human", user_input)]
        print("Messages:", messages)
        ai_msg = llm.invoke(messages)
        print("AI response:", ai_msg.content)
        return jsonify({"response": ai_msg.content})
    return render_template('index.html')

if __name__ == "__main__":
    # TODO Remove debug... Enable in .env
    app.run(debug=True)
