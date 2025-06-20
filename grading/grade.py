import openai
import json
from docx import Document

def grade_transcript(transcript_text, rubric_file):
    """
    Grades the transcript using an LLM based on the uploaded rubric.
    :param transcript_text: Transcript of the student presentation
    :param rubric_file: Uploaded rubric (.docx or .json)
    :return: (dict of scores, summary feedback string)
    """
    rubric_prompt = parse_rubric_to_prompt(rubric_file)

    full_prompt = f"""
    You are a professor grading a student’s video presentation transcript. Use the following rubric:

    {rubric_prompt}

    Transcript:
    {transcript_text}

    Provide:
    1. A score breakdown for each rubric criterion (as a JSON object)
    2. A short paragraph of summary feedback that justifies the score
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a university professor grading presentations."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.4
    )

    output = response["choices"][0]["message"]["content"]
    try:
        json_start = output.find("{")
        json_end = output.find("}
") + 1
        scores = json.loads(output[json_start:json_end])
        feedback = output[json_end:].strip()
    except Exception:
        scores = {}
        feedback = output

    return scores, feedback

def parse_rubric_to_prompt(rubric_file):
    if rubric_file.name.endswith(".json"):
        return rubric_file.read().decode("utf-8")
    elif rubric_file.name.endswith(".docx"):
        doc = Document(rubric_file)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    else:
        raise ValueError("Unsupported rubric file format.")
