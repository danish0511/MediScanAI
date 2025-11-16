# MediScan-AI

MediScan-AI is a prototype multimodal healthcare assistant that combines:
* Speech-to-text (for patient voice input),
* Medical image understanding (e.g., skin rash, acne images), and
* A Large Language Model (LLM) “brain” that generates clinical-style responses, plus text-to-speech output for the doctor’s voice.

---

## Key Features

- Accepts voice + image inputs (patient describes symptoms and/or uploads a medical image).
- Uses OpenAI Whisper (or compatible STT) for high-quality transcription.
- Multimodal LLM backend for image + text understanding (project references Llama 4 Maverick 17B / accelerated inference).
- Text-to-speech for doctor voice (gTTS used in the project).
- Gradio-based UI for an interactive demo.

---

## Architecture & Components

1. **Patient voice capture** → audio file (recording).
2. **Speech-to-text** (OpenAI Whisper or equivalent) → transcript.
3. **Image input** (e.g., acne.jpg, skin_rash.jpg present in repo) → image encoder / LLM input.
4. **LLM Multimodal ‘Brain’** (brain_of_doctor.py) combines transcript + image context → clinical reply.
5. **Text-to-speech** (voice_of_doctor.py using gTTS) renders spoken reply, optionally saved as mp3.
6. **Frontend**: gradio_app.py exposes a UI for voice recording, image upload, and response playback.

## Repository structure

* `gradio_app.py` — Gradio UI / demo launcher.
* `brain_of_doctor.py` — LLM orchestration / multimodal prompt & inference.
* `voice_of_patient.py` — audio capture / preprocessing (patient voice).
* `voice_of_doctor.py` — TTS logic (gTTS examples / saving mp3).
* `Media assets`: acne.jpg, skin_rash.jpg, several example .mp3 files. 
* `Pipfile` / `Pipfile.lock` — project dependencies (environment).

---

##  Running This Locally

Here's how to get everything up and running on your machine:

### 1. Clone the repository

```bash
git clone https://github.com/danish0511/MediScanAI.git
cd MediScanAI
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# or
# venv\Scripts\activate         # Windows

# If you use pipenv:
pipenv install

# Or install common packages manually (example):
pip install gradio gtts openai soundfile numpy pillow

```

### 3. Create .env file
```bash
GROQ_API_KEY=<enter_your_api_key>
```

### 4. Launch the Gradio demo:
```bash
python gradio_app.py
```

The Gradio UI should open locally (e.g. http://127.0.0.1:7860) and allow voice recording, image upload and playback of AI-generated audio responses.

---
