import streamlit as st
import whisper
import torchaudio
import tempfile
import os

st.set_page_config(page_title="🎤 Voice-to-Text Assistant", layout="centered")
st.title("🎤 Open-Source Voice-to-Text Assistant")
st.write("Upload an audio file and get the transcribed text using OpenAI's Whisper model.")

# Upload section
uploaded_file = st.file_uploader("Upload an audio file (MP3/WAV/M4A)", type=["mp3", "wav", "m4a"])

# Load Whisper model only once
@st.cache_resource
def load_model():
    return whisper.load_model("base")

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.audio(uploaded_file, format="audio/wav")

    with st.spinner("Transcribing..."):
        model = load_model()
        result = model.transcribe(temp_path)
        transcription = result["text"]

    st.subheader("📝 Transcribed Text")
    st.success(transcription)

    os.remove(temp_path)