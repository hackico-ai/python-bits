# YouTube Captions Fetcher

## Description

The YouTube Captions Fetcher is a Python script that extracts captions from YouTube videos. It utilizes the `pytube` library to fetch captions in the specified language, defaulting to English.

## Features

- Extract captions from YouTube videos.
- Supports multiple languages.
- Handles errors gracefully.

## Usage

To use the script, modify the `video_id` variable in the `main()` function of `youtube_captions_fetcher.py` with the desired YouTube video ID.

```python
def main():
    video_id = "YOUR_VIDEO_ID"  # Replace with your video ID
    ...
```

## Output example

```SRT
Captions:

1
00:00:00,000 --> 00:00:01,500
Hello, welcome to this tutorial!

2
00:00:02,000 --> 00:00:04,000
In this video, we will learn how to extract YouTube captions.

...
```

## Acknowledgments

- [pytube](https://github.com/nficano/pytube) for the YouTube video downloading library.
