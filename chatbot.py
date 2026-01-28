
from http.client import responses

from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from requests import session
from streamlit import chat_message

#load env
load_dotenv()

#stremlit page setup

st.set_page_config(
    page_title="💬 ChatBot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI ChatBot")

#initiate chat history


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm initiate

llm= ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

#input box
user_prompt = st.chat_input("ask anything...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})

    responses = llm.invoke(
        input=[{"role":"user", "content":"You are helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = responses.content
    st.session_state.chat_history.append({"role":"user", "content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

