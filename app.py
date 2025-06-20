import streamlit as st
from bot import call_groq_gpt
# from dotenv import load_dotenv

# load_dotenv()

st.set_page_config(page_title="🩺 Medical Diagnosis Chatbot", layout="centered")

st.title("🧠 AI Medical Chatbot (Groq)")
st.markdown("Describe your symptoms and get possible disease predictions.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your symptoms:", key="user_input")

if st.button("Diagnose") and user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.spinner("Analyzing..."):
        response = call_groq_gpt(f"I am experiencing the following symptoms: {user_input}. What could be the possible disease?")
        st.session_state.chat_history.append(("Bot", response))

# Display chat
# for sender, message in st.session_state.chat_history:
#     st.chat_message("user" if sender == "You" else "assistant").markdown(f"**{sender}:** {message}")
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div style='text-align: right; color: yellow'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: green'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)

