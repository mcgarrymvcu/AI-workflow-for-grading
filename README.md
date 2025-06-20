# AI Video Grading Assistant

This tool allows instructors to upload student presentation videos and grade them automatically using AI.

1. Extracts audio from `.mp4` files
2. Transcribes audio using OpenAI Whisper
3. Applies grading logic based on a provided rubric
4. Outputs a `.docx` file with score breakdown and feedback

## Setup
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your-api-key-here
streamlit run app.py
```

## Inputs
- `.mp4` student videos
- `.docx` or `.json` rubric

## Output
- Downloadable `.docx` feedback
