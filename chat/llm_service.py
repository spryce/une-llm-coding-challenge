"""
OpenAI based language model service for simple chat application.
Processes user queries and provides historical conversational context using OpenAI's GPT-4 model.
"""

from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from .config import Config

# Store chat session history
chat_session_histories = {}

# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=Config.OPENAI_API_KEY,
)

llm_with_history = RunnableWithMessageHistory(
    llm,
    get_session_history=lambda session_id: chat_session_histories.setdefault(
        session_id, InMemoryChatMessageHistory()
    ),
)


def get_chat_response(session_id, user_input):
    """Process user input and return AI response."""
    messages = [("human", user_input)]
    ai_msg = llm_with_history.invoke(
        messages, config={"configurable": {"session_id": session_id}}
    )
    return ai_msg.content
