import streamlit as st
import requests

# Configura tu API key de ElevenLabs
ELEVENLABS_API_KEY = "sk_628f20d8f86797b404799056f0443d2a4920cadc7cbbbfd1" # Reemplaza con tu API Key real
VOICE_ID = "1Z7qQDyqapTm8qBfJx6e" #INGLES
#VOICE_ID = "tTdCI0IDTgFa2iLQiWu4"  # español

def text_to_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.content  # Devuelve el audio en bytes
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Interfaz en Streamlit
st.title("Texto a Voz con ElevenLabs")

user_text = st.text_area("Escribe el texto que quieres convertir a voz:")

if st.button("Convertir a voz"):
    if user_text.strip():
        audio_data = text_to_speech(user_text)
        if audio_data:
            st.audio(audio_data, format="audio/mp3")
    else:
        st.warning("Por favor, escribe algo de texto.")
