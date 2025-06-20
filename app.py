import streamlit as st
from grading.transcribe_openai import transcribe_video  # Using OpenAI Whisper API
from grading.grade import grade_transcript
from grading.generate_docx import generate_feedback_docx
from utils.ffmpeg_utils import extract_audio
import os
import tempfile

st.title("AI Video Grading Assistant")

uploaded_rubric = st.file_uploader("Upload Rubric (.docx or .json)", type=["docx", "json"])
uploaded_video = st.file_uploader("Upload Student Presentation (.mp4)", type="mp4")

if uploaded_rubric and uploaded_video:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_video.read())
        video_path = temp_video.name

    st.info("Extracting audio...")
    audio_path = extract_audio(video_path)

    st.info("Transcribing video...")
    transcript = transcribe_video(audio_path)
    st.text_area("Transcript Preview", transcript[:2000], height=300)

    st.info("Grading transcript...")
    scores, feedback = grade_transcript(transcript, uploaded_rubric)
    st.write("### Grade Summary")
    st.json(scores)
    st.write("### Feedback")
    st.text(feedback)

    st.info("Generating Word document...")
    output_path = generate_feedback_docx(scores, feedback, transcript)
    with open(output_path, "rb") as f:
        st.download_button("Download Feedback (.docx)", f, file_name="feedback.docx")
