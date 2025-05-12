import os

import streamlit as st
from dotenv import load_dotenv
import google.genai as gen_ai

#loading env variables
load_dotenv()

#configuring streamlit
st.set_page_config(
    page_title="Chat with Google GenAI",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

Google_API_KEY = os.getenv("GOOGLE_API_KEY")

#setting up model
gen_ai.configure(api_key=Google_API_KEY)
model = gen_ai.GenarativeModel('gemini-2.0-flash')

#function to translate roles between streamlit and google genai
def translate_role(role):
    if role == "model":
        return "assistant"
    else:
        return role
    
#initializing session in Streamlit
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#displaying chatbots title
st.title("Chat with Google GenAI")

#displaying chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role(message.role)):
        st.markdown(message.parts[0].text)

#input field for user message
user_prompt = st.chat_input("Ask you question...")
if user_prompt:
    #displaying user message
    with st.chat_message("user"):
        st.markdown(user_prompt)
    
    #sending user message to google genai
    st.session_state.chat_session.send_message(user_prompt)
    
    #getting response from google genai
    response = st.session_state.chat_session.get_response()
    
    #displaying google genai response
    with st.chat_message("model"):
        st.markdown(response.parts[0].text)
