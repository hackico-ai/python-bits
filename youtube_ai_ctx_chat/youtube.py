from pytube import YouTube

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
