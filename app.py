import gradio as gr
from src.concierge_logic import greet

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Ahmed’s AI Concierge™")
    name_input = gr.Textbox(label="What is your name?")
    greet_output = gr.Textbox(label="Ahmed's Greeting")
    greet_button = gr.Button("Greet")

    greet_button.click(
        fn=greet,
        inputs=name_input,
        outputs=greet_output
    )

if __name__ == "__main__":
    import sys
    share = '--share' in sys.argv
    demo.launch(share=share)