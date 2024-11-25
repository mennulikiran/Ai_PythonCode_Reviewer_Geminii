# PyGenAI Code Reviewer 🤖
PyGenAI is an AI-powered Python code reviewer that analyzes Python scripts, identifies bugs and errors, and provides suggestions for improvements. This tool leverages generative AI (Gemini-1.5 Pro) to offer real-time, conversational feedback on your code.

Features 🚀
Real-time Feedback: Get instant code reviews and suggestions.
Bug Detection: Automatically highlights bugs and areas for improvement.
File Upload Support: Upload .py scripts for analysis.
Manual Code Input: Paste your Python code directly into the app for review.
Bug Report & Suggestions: Receive detailed bug reports and improvement suggestions from AI.
Tech Stack 🛠️
Generative AI: Google Gemini-1.5 Pro API
Frontend: Streamlit
Environment: Python
API: Python google.generativeai package
Others: dotenv for environment variable management, os for file handling
Installation 🏗️
To set up the project on your local machine:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/PyGenAI-Code-Reviewer.git
Navigate to the project directory:

bash
Copy code
cd PyGenAI-Code-Reviewer
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables:

Create a .env file in the root directory.
Add your Google Generative AI API key to the .env file:
makefile
Copy code
API_KEY=your_google_api_key
Download the system prompt file (system_prompt.txt) and place it in the root directory.

Run the app:

bash
Copy code
streamlit run app.py
How to Use 🧑‍💻
1. Upload Python Script
Click on the 📄 File Upload tab and upload your Python script (.py file).
Once uploaded, click Analyze Uploaded Script to get feedback and suggestions.
2. Manual Code Input
Click on the ✏️ Manual Input tab.
Paste your Python code into the text area.
Click Analyze Manual Input to receive real-time feedback from the AI.
3. View Feedback
After analyzing the code, the AI will provide feedback on any errors or improvements.
You will also receive a bug report and suggestions for improving the code.
Customization ✨
1. Background Image
To change the background image:

Replace the background: url('your_image_url') in the CSS section with your preferred image URL.
2. API Key
The project requires a Google Generative AI API key. Follow the setup steps to provide your API key in the .env file.
Contributing 🤝
If you would like to contribute to the project, feel free to fork this repository, create a branch, and submit a pull request with your proposed changes.

Please make sure to update the documentation and ensure all tests pass before submitting your changes.

License 📜
This project is licensed under the MIT License - see the LICENSE file for details.
