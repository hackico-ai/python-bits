import openai
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

def create_chatbot_with_context(captions_text):
    def chatbot(message, history):
        history = history or []
        prompt = f"""You are a helpful assistant that answers questions based on the transcript of a YouTube video.

Video Transcript (partial context):
{captions_text[:4000]}

User: {message}
Assistant:"""

        try:
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500
            )
            reply = response.choices[0].message['content'].strip()
        except Exception as e:
            reply = f"OpenAI Error: {str(e)}"

        history.append((message, reply))
        return history, history

    return chatbot
