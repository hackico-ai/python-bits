import gradio as gr
from youtube import get_youtube_captions
from chatbot import create_chatbot_with_context

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 🎥 YouTube GPT Chatbot\nPaste a YouTube video URL and start chatting with the video content!")

        url_input = gr.Textbox(label="YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
        load_btn = gr.Button("Load Video")
        chatbot_ui = gr.Chatbot()
        msg = gr.Textbox(label="Enter your message", interactive=False)
        clear = gr.Button("Clear Chat")

        state = gr.State([])
        chatbot_fn_state = gr.State(None)

        def load_video_and_prepare_chat(video_url):
            captions = get_youtube_captions(video_url)
            if "Error" in captions or "No captions" in captions:
                return gr.update(interactive=False), [], f"⚠️ {captions}", None
            chatbot_fn = create_chatbot_with_context(captions)
            return gr.update(interactive=True), [], "✅ Captions loaded. You can start chatting!", chatbot_fn

        load_btn.click(load_video_and_prepare_chat, inputs=url_input, outputs=[msg, chatbot_ui, url_input, chatbot_fn_state])

        msg.submit(
            lambda message, history, fn: fn(message, history) if fn else (history, history),
            inputs=[msg, state, chatbot_fn_state],
            outputs=[chatbot_ui, state]
        )

        clear.click(lambda: ([], [], ""), None, outputs=[chatbot_ui, state, url_input])

    return demo

if __name__ == "__main__":
    interface = create_interface()
    interface.launch()
