import streamlit as st
import google.generativeai as genai

# ⚠️ WARNING: Embedding API keys directly is not secure for public apps
genai.configure(api_key="AIzaSyAp2T5vBTu2br1u2etEy_178O6M7Xnk464")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("My Gemini Chatbot 🤖")

# Initialize chat messages
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

    # Generate streaming response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in model.generate_content(user_prompt, stream=True):
            if chunk.text:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Optional: Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []

