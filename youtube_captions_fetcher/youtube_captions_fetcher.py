from pytube import YouTube

# =============== Design ===============
def get_youtube_captions(video_url, language="en"):
    """Extract captions from YouTube video URL (default language is English)."""
    
    try:
        yt = YouTube(video_url)

        if language in yt.captions:
            caption = yt.captions[language]
            caption_text = caption.generate_srt_captions()
            return caption_text
        else:
            return f"No captions found for the language: {language}"
    
    except Exception as e:
        return f"Error: {str(e)}"


# =============== Implementation ===============
def main():
    video_id = "my_video_id"

    video_url = f"https://www.youtube.com/watch?v={video_id}"
    language = "en"

    captions = get_youtube_captions(video_url, language)
    if captions:
        print("Captions:\n")
        print(captions)
    else:
        print("No captions available.")

# Usage
if __name__ == "__main__":
    main()

# ******************** Testing ********************

import pytest
from youtube_captions_fetcher import get_youtube_captions

def test_get_youtube_captions_valid():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    language = "en"

    captions = get_youtube_captions(video_url, language)
    assert isinstance(captions, str)  # Check if the result is a string
    assert len(captions) > 0  # Ensure that captions are returned

def test_get_youtube_captions_no_captions():
    video_url = "https://www.youtube.com/watch?v=INVALID_VIDEO_ID"
    language = "en"
    
    result = get_youtube_captions(video_url, language)
    assert result == "No captions found for the language: en"

def test_get_youtube_captions_error_handling():
    video_url = "https://www.youtube.com/watch?v=INVALID_VIDEO_ID"
    language = "fr"
    
    result = get_youtube_captions(video_url, language)
    assert "Error:" in result
