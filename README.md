# Gemini-powered Chatbot 🤖💬

A Streamlit-based web application that allows users to chat with Google's Gemini AI model (Gemini 1.5 Flash). This interactive chatbot maintains conversation history and provides intelligent responses to user queries.

🟢 **Live Demo:** [Click here to try it out](https://building-chatbot-sus.streamlit.app/)  
> ⚠️ *If you see an error after submitting a question, it might be because the API key usage limit has been reached.*

## Features ✨

- 💬 Real-time AI chatbot interaction
- ⚙️ Powered by Google's Gemini 1.5 Flash model
- 🧠 Context-aware conversation using session memory
- 🔐 Secure API key management via `.env`
- ⚡ Fast and responsive interface with Streamlit

## 📁 Project Structure
.
├── app.py # Main application file
├── .env # Environment variable file (should be created by you)
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)

## Prerequisites 🛠️

Before running the application, ensure you have:

- Python 3.7 or higher installed
- A Google API key with access to the Gemini API
- Basic understanding of Python and Streamlit

## Installation ⚙️

Follow these steps to get the project running on your local machine:

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

🙏 Acknowledgements
Google Generative AI – Gemini Model

Streamlit – Web app framework

python-dotenv – Secure environment management

📜 License
This project is licensed under the MIT License.
Feel free to modify and distribute with proper attribution.

📬 Feedback & Contributions
Got ideas or improvements?
Fork this repo, submit a pull request, or open an issue — contributions are always welcome!