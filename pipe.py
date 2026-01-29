import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
import sys

# Accept stdin pipe from bash
piped_text = sys.stdin.read()

# Load credentials from .env
load_dotenv()
eleven_labs_key = os.getenv("ELEVENLABS_KEY")

# Define clients
client = ElevenLabs(api_key=eleven_labs_key)

# Call Elevenlabs API and define voice id
def play_audio(text: str):
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="ava9PNSdpOJuwGttTEgE",      # example premade voice id (Adam)
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
        voice_settings={
            "stability": 1,
            "similarity_boost": 1,
            "speed": 1
        },
    )
    play(audio)

play_audio(piped_text)
