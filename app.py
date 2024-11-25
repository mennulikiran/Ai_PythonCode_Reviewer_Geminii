import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv("API_KEY")

if not api_key:
    st.error("🚨 **API key not found. Please set your API key in a .env file.**")
    st.stop()

# Load system prompt
try:
    with open("system_prompt.txt", "r") as file:
        sys_prompt = file.read()
except FileNotFoundError:
    st.error("🚨 **System prompt file (system_prompt.txt) not found.**")
    st.stop()

# Configure Generative AI
genai.configure(api_key=api_key)

# Initialize the Generative AI model
try:
    model = genai.GenerativeModel(model_name="gemini-1.5-pro", system_instruction=sys_prompt)
except Exception as e:
    st.error(f"🚨 **Error initializing Generative AI model:** {e}")
    st.stop()

# Streamlit app UI customization
st.set_page_config(
    page_title="PyGenAI Code Reviewer", 
    page_icon="🤖", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Add custom CSS styling for background image and overall UI
st.markdown("""
    <style>
        body {
            background: url('https://miro.medium.com/v2/resize:fill:320:214/1*wh3Q-XwQ6UZsJH960bYr-A.png') no-repeat center center fixed;
            background-size: cover;
            color: white;
        }
        .css-18e3th9 {
            background-color: #0c2461;
            color: #ffffff;
        }
        .stButton > button {
            background-color: #38ada9;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.5em 1em;
            font-size: 1.1em;
        }
        .stButton > button:hover {
            background-color: #82ccdd;
            color: black;
        }
        .css-1aumxhk {
            background-color: #0c2461;
        }
        .stSidebar {
            background-color: #0a3d62;
            color: #ffffff;
        }
        .css-1lcbmhc {
            border: 2px solid #38ada9;
            border-radius: 10px;
            padding: 10px;
            color: #ffffff;
        }
        .css-1avcm0n {
            color: #38ada9;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar: App Description
with st.sidebar:
    st.image("https://via.placeholder.com/200x100", use_column_width=True)  # Replace with your own logo
    st.title("📚 About PyGenAI")
    st.markdown(
        """
        **🧑‍💻 PyGenAI** is an AI-powered Python code reviewer that:
        - 🚀 Highlights bugs, errors, and areas for improvement.
        - 📄 Supports file uploads for `.py` scripts or manual code input.
        - 🔁 Streams feedback in real-time for a conversational experience.
        
        ### 💡 **How to Use**:
        1. **Upload a Python script** or paste code directly in the input box.
        2. Click **Analyze** to get AI-powered feedback.
        3. 🎯 Review feedback in the response section.

        ---
        👨‍💻 Created by **Mennuli Kiran** 🚀
        """
    )

# Main Header
st.markdown("<h1 style='text-align: center; color: #82ccdd;'>💻 PyGenAI Code Reviewer 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #c8d6e5;'>Your Personal Python Code Reviewer 🚀</h3>", unsafe_allow_html=True)

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Function to format chat history for AI
def format_history(history):
    return [{"role": entry["role"], "parts": [{"text": entry["content"]}]} for entry in history]

# Function to get AI's response for code review
def get_response(message):
    formatted_history = format_history(st.session_state.history)
    chatbot = model.start_chat(history=formatted_history)
    response = chatbot.send_message(message)

    st.session_state.history.append({"role": "user", "content": message})
    st.session_state.history.append({"role": "model", "content": response.text})

    return response.text

# Function to get bug report and suggestions
def get_bug_report_and_suggestions(code):
    bug_report_prompt = f"Analyze the following Python code and generate a bug report along with suggestions for improvement:\n\n{code}"
    return get_response(bug_report_prompt)

# Section: File Upload or Manual Input
st.markdown("<h2 style='color: #60a3bc;'>Upload Your Code or Paste it Below</h2>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["📄 File Upload", "✏️ Manual Input"])

# Tab 1: File upload
with tab1:
    uploaded_file = st.file_uploader("Upload your Python script", type=["py"])
    if uploaded_file is not None:
        file_content = uploaded_file.read().decode("utf-8")
        st.code(file_content, language="python")

        # Analyze button
        if st.button("Analyze Uploaded Script"):
            with st.spinner("🚀 Analyzing your code..."):
                try:
                    response_text = get_response(file_content)
                    st.markdown("<h3 style='color: #78e08f;'>AI Response</h3>", unsafe_allow_html=True)
                    st.success(response_text)

                    # Bug report and suggestions
                    st.markdown("<h3 style='color: #fad390;'>Bug Report and Suggestions</h3>", unsafe_allow_html=True)
                    bug_report = get_bug_report_and_suggestions(file_content)
                    st.info(bug_report)
                except Exception as e:
                    st.error(f"❌ Error processing your request: {e}")

# Tab 2: Manual input
with tab2:
    user_code = st.text_area("Paste your Python script here:", height=200)
    if st.button("Analyze Manual Input"):
        with st.spinner("🚀 Analyzing your code..."):
            try:
                response_text = get_response(user_code)
                st.markdown("<h3 style='color: #78e08f;'>AI Response</h3>", unsafe_allow_html=True)
                st.success(response_text)

                # Bug report and suggestions
                st.markdown("<h3 style='color: #fad390;'>Bug Report and Suggestions</h3>", unsafe_allow_html=True)
                bug_report = get_bug_report_and_suggestions(user_code)
                st.info(bug_report)
            except Exception as e:
                st.error(f"❌ Error processing your request: {e}")

# Footer
st.markdown(
    """
    ---
    <div style='text-align: center;'>
        Made with ❤️ by <strong>Mennuli Kiran</strong> | 
        <a href='https://www.linkedin.com/in/kiran-mennuli-637322250/' style='color: #78e08f;'>GitHub</a> | 
        <a href='https://github.com/mennulikiran?tab=repositories' style='color: #78e08f;'>LinkedIn</a>
    </div>
    """, 
    unsafe_allow_html=True
)
