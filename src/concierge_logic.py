import random

# A mock knowledge base of Dubai tours and experiences.
# In a real application, this would come from a database or CMS.
KNOWLEDGE_BASE = {
    "burj khalifa": {
        "response": "Ah, the Burj Khalifa, a true titan of the skyline. It’s more than just the world's tallest building; it’s a testament to Dubai's ambition. The view from the top, especially as the sun sets and the city lights begin to twinkle, is a memory that will stay with you forever.",
        "tip": "For a truly exclusive experience, book the 'At the Top, SKY' lounge. It's on a higher floor with fewer crowds and includes complimentary refreshments. The perfect way to soak in the view in style."
    },
    "desert safari": {
        "response": "The desert safari is an essential Dubai adventure. Imagine gliding over golden dunes, the silence of the desert broken only by the whisper of the wind. It’s a journey into the heart of Arabian heritage, culminating in a starlit dinner and traditional entertainment.",
        "tip": "Ask for the 'platinum' safari option. It often includes a private vehicle and a more authentic camp experience, away from the larger, more crowded tour groups."
    },
    "default": {
        "response": "A fascinating question. Dubai is a city of countless stories. Could you perhaps ask me about a specific landmark or experience, such as the 'Burj Khalifa' or a 'desert safari'?",
        "tip": "The best time to explore Dubai is from November to March when the weather is absolutely sublime and perfect for outdoor adventures."
    }
}

def get_concierge_response(user_query: str) -> tuple[str, str]:
    """
    Analyzes a user's query and returns a story-driven response and an "Ahmed's Tip™".

    Args:
        user_query: The question from the user.

    Returns:
        A tuple containing the main response and the tip.
    """
    if not user_query:
        # Initial greeting if the query is empty
        return (
            "Welcome to Ahmed’s AI Concierge™. I am here to help you unlock the soul of Dubai. What adventure are you dreaming of today?",
            "For the most breathtaking photos, the golden hour just before sunset bathes the city in a magical light. It's a photographer's dream."
        )

    query = user_query.lower()

    for keyword, data in KNOWLEDGE_BASE.items():
        if keyword in query:
            return data["response"], data["tip"]

    # If no keyword is found, return a default response
    return KNOWLEDGE_BASE["default"]["response"], KNOWLEDGE_BASE["default"]["tip"]