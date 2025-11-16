# Step1: Setup Text to Speech TTS model (gTTS and ElevenLabs)
# with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"
    
    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

# input_text="Hi this is Generative AI project"
# text_to_speech_with_gtts_old(input_text, "gtts_test1.mp3")

# Step2: Use model for text output to voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"
    
    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# input_text="Hi this is Generative AI project autoplay test"
# text_to_speech_with_gtts(input_text, "gtts_autoplay_test1.mp3")
