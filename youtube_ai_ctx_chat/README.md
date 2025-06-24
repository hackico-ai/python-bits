# YouTube GPT Chatbot

## Description

AI chatbot template for analyzing video content. It helps researchers explore, study, and interact with YouTube videos. Using automatic caption extraction and OpenAI’s language models, it generates natural, informative conversations based on the video’s content—making it a powerful tool for research, learning, and content analysis.

## Features

- Extracts YouTube captions in a specified language (default: English)
- Integrates OpenAI's ChatGPT to enable contextual Q&A
- Interactive web-based chatbot using Gradio
- Modular codebase for easy extension
- Select OpenAI GPT model from configuration

## Tool Structure

youtube_ai_ctx_chat/
├── app.py # Main Gradio interface
├── chatbot.py # GPT/OpenAI interaction logic
├── youtube.py # YouTube caption extractor
└── config.py # Configuration (OpenAI API key, model name)

## Usage

### 1. Set up your environment

Install required packages:

pip install gradio openai pytube
Add your OpenAI API key and preferred GPT model in config.py:

### config.py

```python
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "your-api-key-here"
MODEL_NAME = os.getenv("OPENAI_MODEL") or "gpt-3.5-turbo"  # e.g., "gpt-4"
You can also set these as environment variables:
```

### shell

```bash
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_MODEL="gpt-4"
```

### 2. Run the app

```bash
python app.py
```

A browser window will open with an interactive chatbot. Paste a YouTube video URL, load captions, and ask questions about the video’s content!

Output Example

```
# Chat Interface:

User: What is the video about?
Assistant: The video discusses how neural networks learn from data...
```

Caption Sample Output:

```
SRT

1
00:00:00,000 --> 00:00:01,500
Hello, welcome to this tutorial!

2
00:00:02,000 --> 00:00:04,000
In this video, we will learn how to extract YouTube captions.
```

## Acknowledgments

- pytube for YouTube caption extraction
- OpenAI for the GPT language model API
- Gradio for the interactive user interface
