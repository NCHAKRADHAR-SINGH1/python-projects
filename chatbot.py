import streamlit as st
import google.generativeai as genai

# Set your Gemini API key directly here (⚠ keep private)
genai.configure(api_key="AIzaSyAp2T5vBTu2br1u2etEy_178O6M7Xnk464")

# Choose the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("My Own Gemini Chatbot 🤖")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input

if user_prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate streaming response from Gemini
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Streaming with Gemini
        for chunk in model.generate_content(user_prompt, stream=True):
            if chunk.text:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})