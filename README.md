**TalentScout - Hiring Assistant Chatbot**

**Project Overview**

TalentScout is an AI-powered hiring assistant chatbot designed to streamline the technical interview preparation process for candidates. Built using Streamlit and Gemini AI, it collects candidate details, generates technical interview questions based on their tech stack, maintains conversation context, and provides structured interview guidance.

**Installation Instructions**

**Prerequisites**

Ensure you have the following installed on your system:

Python 3.8+

pip (Python package manager)

A Google Gemini AI API key

Setup Steps

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install dependencies**

pip install -r requirements.txt

Set up environment variables

Create a .env file in the project root directory and add your Google Gemini API key:

GEMINI_API_KEY=your_api_key_here

**Run the application**

streamlit run app.py

**Usage Guide**

Open the chatbot UI in your web browser.

Fill out the form with your details, including tech stack.

View generated technical interview questions tailored to your skills.

Ask follow-up questions in the chatbot input field.

Click the "End Conversation" button to conclude the session.

**Technical Details**

Libraries Used

streamlit - UI framework for web applications.

google-generativeai - API client for Gemini AI.

dotenv - Loads environment variables from a .env file.

json - Used for handling structured data.

**Model Details**

Gemini AI: Used to generate contextual responses and technical interview questions based on user input.

**Architectural Decisions**

Streamlit UI: Chosen for its simplicity and rapid prototyping capabilities.

Session-based context handling: Ensures coherent chatbot conversations.

Prompt engineering: Ensures generated responses are relevant and structured.

**Prompt Design**

The chatbot uses structured prompts to generate responses effectively:

Greeting prompt: Welcomes the user and explains functionality.

Technical question generation prompt: Ensures responses align with the candidate's experience and tech stack.

Context handling prompt: Maintains conversation continuity.

Fallback prompt: Provides relevant responses when unexpected input is received.

**Challenges & Solutions**

1. Maintaining Context in Conversations

Challenge: Ensuring the chatbot remembers prior messages for coherent responses.

Solution: Implemented a conversation history list with a rolling window to store the last few interactions.

2. Generating Precise Technical Questions

Challenge: Ensuring relevant and structured questions for various tech stacks.

Solution: Crafted detailed prompts that explicitly ask for five questions in a predefined format.

3. Handling Unexpected Inputs

Challenge: Avoiding irrelevant or off-topic responses.

Solution: Implemented fallback responses and limited chatbot scope to hiring-related queries.

Future Enhancements

Add database storage for candidate records.

Improve UI with better styling and interactivity.

Expand support for more conversational capabilities.

