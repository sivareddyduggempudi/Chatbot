import json
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.0-pro-exp-02-05")

# Function to get model response
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to maintain conversation context
conversation_history = []
def maintain_context(user_input):
    conversation_history.append(user_input)
    if len(conversation_history) > 5:  # Limit history length
        conversation_history.pop(0)
    context = "\n".join(conversation_history)
    
    # Generate a response based on context
    prompt = f"""
    You are an AI assistant helping with job applications and interview preparation.
    Maintain the context of the conversation and provide relevant responses.
    If the user asks about their responsibilities for a job, generate a response based on a technology-related role.
    Current conversation:
    {context}
    Respond appropriately:
    """
    return get_gemini_response(prompt)

# Streamlit form for candidate input
def gather_candidate_info():
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (comma-separated)")
        submit_button = st.form_submit_button("Submit")
    st.write("Fill out the form above to generate interview questions! Once generated, they will be displayed below.")

    if submit_button:
        candidate_data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "experience": int(experience),
            "position": position,
            "location": location,
            "tech_stack": [tech.strip() for tech in tech_stack.split(",") if tech.strip()]
        }
        st.session_state["candidate"] = candidate_data
        return candidate_data
    return None

# Function to generate technical questions
def generate_technical_questions(tech_stack, experience):
    if not tech_stack:
        return "No tech stack provided."

    tech_list = ", ".join(tech_stack)
    prompt = f"""
    You are an expert interviewer. Generate exactly 5 **technical interview questions** for a candidate skilled in **{tech_list}**.
    The candidate has **{experience} years of experience**. 
    
    Format the output as follows:
    
    1. **[Technology]:** Question text
    2. **[Technology]:** Question text
    3. **[Technology]:** Question text
    4. **[Technology]:** Question text
    5. **[Technology]:** Question text
    """
    
    response = get_gemini_response(prompt)
    return response

# Function to handle chatbot greetings
def chatbot_greeting():
    return "Hello! Welcome to TalentScout - Hiring Assistant Chatbot. I will help you with technical interview preparation. Let's get started!"

# Function to handle fallback responses
def fallback_response():
    return "I'm sorry, I didn't understand that. Please provide the requested details or ask relevant questions related to job applications and interviews."

# Function to gracefully end the conversation
def end_conversation():
    return "Thank you for using TalentScout! We appreciate your time. Your details have been recorded, and you will be contacted for the next steps soon. Have a great day!"

# Streamlit UI
st.title("TalentScout - Hiring Assistant Chatbot")

# Display chatbot greeting
st.write(chatbot_greeting())

# Check session state for candidate data
if "candidate" not in st.session_state:
    candidate = gather_candidate_info()
else:
    candidate = st.session_state["candidate"]

if candidate:
    st.subheader("Candidate Information")
    st.json(candidate)

    st.subheader("Generated Technical Questions")
    questions = generate_technical_questions(candidate["tech_stack"], candidate["experience"])
    st.write(questions)

# Chat Input for maintaining conversation context
user_input = st.text_input("Ask a follow-up question or provide additional details:")
if user_input:
    response = maintain_context(user_input)
    st.write(response)

# End conversation button
if st.button("End Conversation"):
    st.write(end_conversation())

if __name__ == "__main__":
    st.write("")
