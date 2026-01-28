import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from openai import OpenAI
from dotenv import load_dotenv
from art import text2art

# Load credentials from .env
load_dotenv()
openai_key = os.getenv("OPENAI_KEY")
eleven_labs_key = os.getenv("ELEVENLABS_KEY")

# Define clients
prompt_client = OpenAI(api_key=openai_key)
client = ElevenLabs(api_key=eleven_labs_key)

# Swag
def pyrate_logo():
    logo_text = "PYRATE"
    logo = text2art(logo_text, font='small')
    print(logo)
    print('Pirate Joke Generator')
    print('by AMP Studios')
pyrate_logo()

# Call OpenAI service and generate pirate joke
def get_joke():
    created_joke = prompt_client.responses.create(
        model = "gpt-5-mini",
        input = "You are a deranged pirate, tell me a joke about the life at sea."
    )
    return created_joke.output_text

# Call joke function and store as a variable
print('Dialing OpenAI hotline...')
joke = get_joke()
print('Joke received!!')

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

# Call play audio function, this will generate temp.mp3 and requires ffmpeg to play
print('Sending joke via carrier pigeon to Eleven Labs HQ!')
play_audio(joke)
