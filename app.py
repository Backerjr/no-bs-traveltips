import gradio as gr
from src.concierge_logic import get_concierge_response

# --- UI Text Translations ---
UI_TEXT = {
    "en": {
        "title": "Ahmed’s AI Concierge™",
        "chatbot_label": "Conversation with Ahmed",
        "input_label": "Your Message",
        "input_placeholder": "e.g., Tell me about the Burj Khalifa...",
    },
    "ar": {
        "title": "أحمد - مساعدك الذكي™",
        "chatbot_label": "محادثة مع أحمد",
        "input_label": "رسالتك",
        "input_placeholder": "مثال: أخبرني عن برج خليفة...",
    }
}

def chat_response(message, history, language):
    """
    Handles the chat interaction, gets the response and tip in the correct language,
    and formats them for the UI.
    """
    history.append({"role": "user", "content": message})
    response, tip, tip_title = get_concierge_response(message, language)
    history.append({"role": "assistant", "content": response})

    tip_card_html = f"""
    <div style="border-left: 5px solid #D4AF37; background-color: #fefdf5; padding: 15px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <strong style="color: #c8a02a; font-family: 'Playfair Display', serif; font-size: 1.1rem;">{tip_title}</strong>
        <p style="margin-top: 8px; color: #2C3E50;">{tip}</p>
    </div>
    """
    return "", history, tip_card_html

def update_ui_language(language):
    """
    Updates all UI text components based on the selected language.
    """
    lang_code = "en" if language == "English" else "ar"
    return (
        gr.update(label=UI_TEXT[lang_code]["chatbot_label"]),
        gr.update(label=UI_TEXT[lang_code]["input_label"], placeholder=UI_TEXT[lang_code]["input_placeholder"]),
    )

# --- Gradio Interface Definition ---
with gr.Blocks(css="assets/style.css", theme=gr.themes.Soft()) as demo:
    # State to hold the current language
    language_state = gr.State("en")

    gr.Markdown(f"""
    <div style="text-align: center; padding-bottom: 10px;">
        <h1 style="font-family: 'Playfair Display', serif; color: #1A237E;">{UI_TEXT['en']['title']} / {UI_TEXT['ar']['title']}</h1>
    </div>
    """)

    lang_selector = gr.Radio(
        ["English", "العربية"],
        value="English",
        label="Language / اللغة",
        info="Select your preferred language."
    )

    chatbot = gr.Chatbot(
        label=UI_TEXT["en"]["chatbot_label"],
        height=400,
        bubble_styling={"template": "soft"}
    )
    msg_input = gr.Textbox(
        label=UI_TEXT["en"]["input_label"],
        placeholder=UI_TEXT["en"]["input_placeholder"],
        scale=3
    )
    tip_output = gr.Markdown()

    # Link the language selector to the UI update function
    lang_selector.change(
        fn=update_ui_language,
        inputs=lang_selector,
        outputs=[chatbot, msg_input]
    )

    # Link the language selector to the language state
    @lang_selector.change(inputs=lang_selector)
    def update_lang_state(language):
        return "en" if language == "English" else "ar"

    # Link the chat submission to the response function
    msg_input.submit(
        fn=chat_response,
        inputs=[msg_input, chatbot, language_state],
        outputs=[msg_input, chatbot, tip_output]
    )

if __name__ == "__main__":
    import sys
    share = '--share' in sys.argv
    demo.launch(share=share)