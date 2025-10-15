import random

# A multilingual knowledge base for Dubai tours and experiences.
KNOWLEDGE_BASE = {
    "burj khalifa": {
        "en": {
            "response": "Ah, the Burj Khalifa, a true titan of the skyline. It’s more than just the world's tallest building; it’s a testament to Dubai's ambition. The view from the top, especially as the sun sets and the city lights begin to twinkle, is a memory that will stay with you forever.",
            "tip": "For a truly exclusive experience, book the 'At the Top, SKY' lounge. It's on a higher floor with fewer crowds and includes complimentary refreshments. The perfect way to soak in the view in style."
        },
        "ar": {
            "response": "أهلاً بك في برج خليفة، الصرح الشاهق الذي يلامس عنان السماء. هو ليس مجرد أطول مبنى في العالم، بل شهادة حية على طموح دبي الذي لا يعرف حدوداً. إن منظر المدينة من القمة، خاصةً عند غروب الشمس بينما تتلألأ الأضواء، هو ذكرى ستظل محفورة في وجدانك إلى الأبد.",
            "tip": "لتجربة استثنائية بكل معنى الكلمة، قم بحجز ردهة 'At the Top, SKY'. تقع في طابق أعلى وتكون أقل ازدحاماً، مع تقديم المرطبات مجاناً. إنها الطريقة المثلى للاستمتاع بالمنظر بأناقة ورفاهية."
        }
    },
    "desert safari": {
        "en": {
            "response": "The desert safari is an essential Dubai adventure. Imagine gliding over golden dunes, the silence of the desert broken only by the whisper of the wind. It’s a journey into the heart of Arabian heritage, culminating in a starlit dinner and traditional entertainment.",
            "tip": "Ask for the 'platinum' safari option. It often includes a private vehicle and a more authentic camp experience, away from the larger, more crowded tour groups."
        },
        "ar": {
            "response": "رحلة السفاري في الصحراء هي مغامرة لا غنى عنها في دبي. تخيل نفسك تنساب فوق الكثبان الذهبية، حيث لا يكسر صمت الصحراء المهيب سوى همس الرياح. إنها رحلة إلى قلب التراث العربي الأصيل، تُتوّج بعشاء فاخر تحت النجوم وعروض ترفيهية تقليدية.",
            "tip": "اطلب خيار السفاري 'البلاتيني'. غالباً ما يتضمن سيارة خاصة وتجربة مخيم أكثر أصالة، بعيداً عن المجموعات السياحية الكبيرة والمزدحمة."
        }
    },
    "default": {
        "en": {
            "response": "A fascinating question. Dubai is a city of countless stories. Could you perhaps ask me about a specific landmark or experience, such as the 'Burj Khalifa' or a 'desert safari'?",
            "tip": "The best time to explore Dubai is from November to March when the weather is absolutely sublime and perfect for outdoor adventures."
        },
        "ar": {
            "response": "سؤالك شيّق بالفعل. دبي مدينة تحفل بالحكايات التي لا تنتهي. هلّا سألتني عن معلم معين أو تجربة فريدة، مثل 'برج خليفة' أو 'رحلة سفاري في الصحراء'؟",
            "tip": "أفضل وقت لاستكشاف دبي هو من شهر نوفمبر إلى مارس، حيث يكون الطقس في أروع حالاته ومثالياً للمغامرات في الهواء الطلق."
        }
    },
    "greeting": {
        "en": {
            "response": "Welcome to Ahmed’s AI Concierge™. I am here to help you unlock the soul of Dubai. What adventure are you dreaming of today?",
            "tip": "For the most breathtaking photos, the golden hour just before sunset bathes the city in a magical light. It's a photographer's dream."
        },
        "ar": {
            "response": "أهلاً بك في خدمة 'أحمد - مساعدك الذكي'™. أنا هنا لمساعدتك على اكتشاف روح دبي الأصيلة. عن أي مغامرة تحلم اليوم؟",
            "tip": "لالتقاط أروع الصور، فإن 'الساعة الذهبية' قبيل غروب الشمس تغمر المدينة بضوء ساحر. إنها لحظة يحلم بها كل مصور."
        }
    }
}

def get_concierge_response(user_query: str, language: str = "en") -> tuple[str, str, str]:
    """
    Analyzes a user's query and returns a story-driven response and an "Ahmed's Tip™"
    in the specified language.

    Args:
        user_query: The question from the user.
        language: The selected language ('en' or 'ar').

    Returns:
        A tuple containing the main response, the tip, and the translated "Ahmed's Tip" title.
    """
    tip_title = "Ahmed's Tip™" if language == "en" else "نصيحة أحمد™"

    if not user_query:
        # Initial greeting if the query is empty
        data = KNOWLEDGE_BASE["greeting"][language]
        return data["response"], data["tip"], tip_title

    query = user_query.lower()

    # Simple keyword matching for English queries
    keyword_map = {
        "burj khalifa": "burj khalifa",
        "safari": "desert safari"
    }

    matched_key = "default"
    for keyword, key in keyword_map.items():
        if keyword in query:
            matched_key = key
            break

    data = KNOWLEDGE_BASE[matched_key][language]
    return data["response"], data["tip"], tip_title