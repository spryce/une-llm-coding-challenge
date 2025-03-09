"""Define routes for the chat UI."""

import uuid
from flask import Blueprint, request, jsonify, render_template, session
from .llm_service import get_chat_response

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    """Render the chatbot UI."""
    return render_template("index.html")


@main.route("/chat", methods=["POST"])
def chat():
    """Handle user query and return model response."""
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())

    session_id = session["session_id"]
    print("Session ID:", session_id)

    user_input = request.form["user_input"]
    if not user_input:
        return jsonify({"error": "User input is required"}), 400
    print("User input:", user_input)

    response = get_chat_response(session_id, user_input)
    print("AI response:", response)

    return jsonify({"response": response, "session_id": session_id})
