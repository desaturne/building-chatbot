# building chatbot

# Gemini-powered Chatbot 🤖💬

A Streamlit-based web application that allows users to chat with Google's Gemini AI model (Gemini 1.5 Flash). This interactive chatbot maintains conversation history and provides intelligent responses to user queries.

## Features ✨

- **Conversational AI**: Powered by Google's Gemini 1.5 Flash model
- **Chat Interface**: Clean, user-friendly interface with message history
- **Session Management**: Maintains conversation history throughout the session
- **Responsive Design**: Adapts to different screen sizes with Streamlit's layout options

## Prerequisites 🛠️

Before running the application, ensure you have:

- Python 3.7 or higher installed
- A Google API key with access to the Gemini API
- Basic understanding of Python and Streamlit

## Installation ⚙️

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot

2. Create and activate a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Create a .env file in the root directory and add your Google API key:
    env
    Google_API_key=your-api-key-here

## Usage
Run the Streamlit application:

    ```bash
    streamlit run app.py

The application will automatically open in your default web browser
Type your message in the chat input box and press Enter to get responses from the Gemini AI
The conversation history will be maintained throughout your session