import gradio as gr
from src.concierge_logic import get_concierge_response

def chat_response(message, history):
    """
    Handles the chat interaction, gets the response and tip,
    and formats them for the UI using the modern 'messages' format.
    """
    # Append the user's message to the history
    history.append({"role": "user", "content": message})

    # Get the narrative response and the tip from our logic module
    response, tip = get_concierge_response(message)

    # Append the assistant's response to the history
    history.append({"role": "assistant", "content": response})

    # Format the "Ahmed's Tip™" as a distinct, styled HTML card
    tip_card_html = f"""
    <div style="border-left: 5px solid #D4AF37; background-color: #fefdf5; padding: 15px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <strong style="color: #c8a02a; font-family: 'Playfair Display', serif; font-size: 1.1rem;">Ahmed's Tip™</strong>
        <p style="margin-top: 8px; color: #2C3E50;">{tip}</p>
    </div>
    """

    # We return an empty string to clear the input box, the updated history, and the tip card
    return "", history, tip_card_html

# --- Gradio Interface Definition ---
with gr.Blocks(css="assets/style.css", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <div style="text-align: center; padding-bottom: 20px;">
        <h1 style="font-family: 'Playfair Display', serif; color: #1A237E;">Ahmed’s AI Concierge™</h1>
    </div>
    """)

    # Use the modern 'messages' format for the chatbot
    chatbot = gr.Chatbot(
        label="Conversation with Ahmed",
        height=400,
        bubble_styling={"template": "soft"} # Use a softer, more modern bubble style
    )
    msg_input = gr.Textbox(label="Your Message", placeholder="e.g., Tell me about the Burj Khalifa...", scale=3)

    # A dedicated area to display the tip
    tip_output = gr.Markdown()

    # When the user submits their message, call the chat_response function
    msg_input.submit(
        fn=chat_response,
        inputs=[msg_input, chatbot],
        outputs=[msg_input, chatbot, tip_output]
    )

if __name__ == "__main__":
    import sys
    share = '--share' in sys.argv
    demo.launch(share=share)