import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import tempfile
st.title("🎤 Speech-to-Text & Text-to-Speech App")
st.header("🗣 Speech to Text")
if st.button("🎙 Start Recording"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now")
        audio = r.listen(source)
        st.write("Processing...")

        try:
            text = r.recognize_google(audio)
            st.success(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Could not request results. Check internet connection.")

# ---------------- Text to Speech ----------------
st.header("💬 Text to Speech")
user_text = st.text_area("Enter text to convert to speech:")

if st.button("🔊 Convert to Speech"):
    if user_text.strip() != "":
        tts = gTTS(user_text)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_file.name)

        # Read file as bytes for Streamlit
        with open(tmp_file.name, "rb") as f:
            audio_bytes = f.read()

        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("Please enter some text to convert.")


