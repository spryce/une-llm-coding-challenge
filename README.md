# UNE LLM Coding Challenge Response

This project is a simplified Flask-based prototype of a system that interacts with an LLM via the OpenAI API.


## Cloning the Repository

To clone the repository, run the following command:

```bash
git clone https://github.com/spryce/une-llm-coding-challenge.git
cd une-llm-coding-challenge
```

## Virtual Environment Setup

It is strongly recommended to setup a virtual environment before installing dependencies. This will keep the project's dependencies separate from your systems global packages:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

## Installing Dependencies

Once the virtual environment is activated, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Configure Environmental Variables 

You must create a .env file in the root of the project and add the following keys:
```
OPENAI_API_KEY=your-openai-key
FLASK_SECRET_KEY=super-secret-key
```
An example file named `.env.example` is available in the root directory
1. OpenAI API Key: This project uses GPT-4o explicitly. Your key must support this model. Some free OpenAI keys are currently restricted to GPT-4o-mini
2. Flask secret key: Used for Flask session management. Any string will be suitable for testing.

## Running the Application

To run the Flask application, use the following command:

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## Additional Information

- Flask reccommends using the latest version of Python and supports 3.9 or above. 
- This application was developed on Python 3.12
- This application uses the LangChain open-source framework for implementing conversation history

## Testing the Application

Run the application using `flask run` from inside the project directory. Test the conversation history by providing information and querying the provided information. 

User prompts:

1. My favourite colour is red. 
2. What is my favourite colour?

`AI response: Your favourite colour is red.`

The system can handle multiple unique users, but we haven't developed authentication for users yet. 
To test unique sessions from your local machine:
- Open a tab *in a different browser* and navigate to `http://127.0.0.1:5000/`. 
- Test with similar prompts

User 2 prompts (from a different browser e.g. Chrome vs Firefox):

1. My favourite colour is blue. 
2. What is my favourite colour?

`AI response: Your favourite colour is blue.`

User 1:
1. What is my favourite colour?

`AI response: Your favourite colour is red.`

User 1's favourite colour is still red, confirming each user has a different session and contextual chat history.

## Project Assumptions

- I assume this application is only intended to be run using Flask's internal development server. It has not been configured and tested on a WSGI production server.
- I'm not aware of UNE policies so I have included an MIT license to avoid any issues.

## Future Improvements

Listing potential improvements here as I think of them and will implement some if time permits.

- Choose a different package manager for better dependancy management
- Allow users to select from other OpenAI models (or other vendors)
- Error handling. Inform the user e.g. 'You exceeded your current quota, please check your plan and billing'
- Predicted Outputs (e.g.code refactoring): https://platform.openai.com/docs/guides/predicted-outputs
- Add auto-tracing with Langsmith
- Add support for dev and prod environments
- Better conversation management to save tokens
- Sanitize input
- Filter messages: https://python.langchain.com/docs/how_to/filter_messages/
- Trim messages: https://python.langchain.com/docs/how_to/trim_messages/
- Throttle input
- Store chat/session history in a database
- Implement user authentication to support persistent chat history
- Allow users to reset their session manually
- Setup a docker file for production env
- Format the AI response
- Display a running chat history 

## Commit History

This repository uses GitFlow. Detailed commit history is available on the Develop branch
