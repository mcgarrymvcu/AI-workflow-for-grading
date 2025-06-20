from moviepy.editor import VideoFileClip
import tempfile

def extract_audio(video_path):
    """
    Extracts audio from a video file using moviepy (no system ffmpeg required).
    :param video_path: Path to the input video file (.mp4)
    :return: Path to the extracted .wav audio file
    """
    try:
        output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(
            output_path,
            fps=16000,
            nbytes=2,
            codec='pcm_s16le',
            ffmpeg_params=["-ac", "1"]
        )
        return output_path
    except Exception as e:
        raise RuntimeError(f"Audio extraction failed: {e}")
