import gradio as gr
import random
from agents.storyteller import StorytellerAgent
from agents.sales import SalesAgent
from agents.branding import BrandingAgent

# --- Instantiate Agents ---
storyteller = StorytellerAgent()
sales = SalesAgent()
branding = BrandingAgent()

# --- Knowledge Bank ---
KNOWLEDGE = {
    "Desert Safari": {
        "description": "A golden hour adventure through the dunes — dune bashing, sandboarding, and a private Bedouin camp with live BBQ.",
        "official_price": "299 AED",
        "exclusive_price": "255 AED",
    },
    "Lotus Mega Yacht Dinner": {
        "description": "A 4-deck yacht cruise with international buffet, live music, and panoramic skyline views.",
        "official_price": "320 AED",
        "exclusive_price": "280 AED",
    },
    "Burj Khalifa SKY 148": {
        "description": "The highest observation deck in Dubai, complete with lounge access and VIP entry.",
        "official_price": "553 AED",
        "exclusive_price": "495 AED",
    },
    "The View at The Palm": {
        "description": "A breathtaking panorama from Nakheel Tower, offering a full view of Palm Jumeirah.",
        "official_price": "120 AED",
        "exclusive_price": "99 AED",
    }
}

# --- Core Chat Logic ---
def chat_fn(message, history):
    found = [exp for exp in KNOWLEDGE if exp.lower() in message.lower()]

    # If the guest mentions a known experience
    if found:
        lines = []
        for name in found:
            exp = KNOWLEDGE[name]
            description = storyteller.describe(name)
            quote = sales.quote(name, exp["official_price"], exp["exclusive_price"])
            lines.append(f"**{name}**\n{description}\n\n{quote}")
        response = "\n\n---\n\n".join(lines)
        return branding.polish(response)

    # Otherwise, give a friendly, on-brand reply
    fallback = random.choice([
        f"Ah, *{message}* — sounds like the start of a great story. Are you thinking culture, adventure, or skyline views?",
        f"You mentioned *{message}*. My instinct? Something refined, warm, and unforgettable.",
        f"For *{message}*, I’d suggest something scenic — where the view tells its own story.",
    ])
    return branding.polish(fallback)

# --- Gradio UI ---
demo = gr.ChatInterface(
    fn=chat_fn,
    title="Ahmed’s AI Concierge™",
    description="Luxury Travel | Storytelling | AI-Optimized Experiences™",
    theme="soft"
)

demo.launch()
