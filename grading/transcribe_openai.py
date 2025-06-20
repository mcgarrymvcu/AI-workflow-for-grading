import openai
import os

def transcribe_video(audio_path):
    """
    Transcribes the audio file using OpenAI Whisper API.
    :param audio_path: Path to the extracted audio file (.wav or .mp3)
    :return: Transcript text as a string
    """
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return transcript["text"]
    except Exception as e:
        return f"Transcription failed: {str(e)}"
