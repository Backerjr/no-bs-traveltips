 feat/initial-project-structure
---
title: Ahmed’s AI Concierge™
emoji: 🐪✨
colorFrom: "#1A237E"
colorTo: "#D4AF37"
sdk: gradio
sdk_version: 4.29.0
app_file: app.py
pinned: false
---

# **Ahmed’s AI Concierge™**

Welcome to Ahmed’s AI Concierge™, a luxury travel assistant that combines poetic storytelling with practical travel info about Dubai and the UAE.

This interactive application provides story-driven insights into Dubai's most iconic experiences and offers personalized tips to make your journey unforgettable.

## **How to Use**
1.  Select your preferred language (English or Arabic).
2.  Ask about a specific landmark, like the "Burj Khalifa" or a "desert safari".
3.  Receive a narrative response and a special "Ahmed's Tip™".
4.  Use the WhatsApp link to contact Ahmed directly and arrange your private tour.

## **Deployment on Hugging Face Spaces**

This application is configured for easy deployment on Hugging Face Spaces.

### **Setup Steps:**
1.  **Create a Hugging Face Account:** If you don't have one, sign up at [huggingface.co](https://huggingface.co).
2.  **Create a New Space:**
    *   Click on your profile picture and select "New Space".
    *   Give your Space a name (e.g., `Ahmed-AI-Concierge`).
    *   Select "Gradio" as the SDK.
    *   Choose "Public" for visibility.
    *   Click "Create Space".
3.  **Upload Files:**
    *   In your new Space, navigate to the "Files" tab.
    *   Upload the entire project directory, ensuring the following are included:
        *   `app.py`
        *   `README.md` (this file)
        *   `requirements.txt`
        *   The `src/` directory
        *   The `assets/` directory
    *   The Space will automatically build and launch the application.

### **Branding (Logo & Favicon):**
*   **Favicon:** To add a custom favicon, place an image file named `favicon.ico` inside the `assets/` directory.
*   **Logo:** To add a logo to the header, place your logo image (e.g., `logo.png`) in the `assets/` directory and update the `gr.Markdown` component in `app.py` to reference it.
    *   Example: `<img src="file/assets/logo.png" alt="Ahmed’s AI Concierge Logo" style="width: 150px;"/>`

---
*This application was developed with the assistance of Jules, an AI project strategist.*

# 💼 Ahmed’s AI Concierge™

**Luxury Travel | Storytelling | AI-Optimized Experiences™**

Ahmed’s AI Concierge™ is an interactive travel assistant built with **Gradio + Python**, designed to bring the warmth, wit, and precision of a real Dubai travel expert into a digital experience.

It blends **poetic storytelling** with **practical trip planning** — offering exclusive prices, insider tips, and beautifully phrased advice that sounds human, not robotic.

---

## ✨ Overview

> “Luxury travel meets storytelling — every reply should feel like a personal note from a trusted Dubai insider.”

This app acts as your on-demand concierge:
- 💬 Chat naturally about UAE experiences  
- 💎 Get **official vs. exclusive rates** instantly  
- 🏝️ Learn what to wear, when to go, and how to make it unforgettable  
- 🧭 Receive **Ahmed’s Tip™** — short, curated insights that make every tour feel bespoke  

---

## 🧠 Features

| Feature | Description |
|----------|-------------|
| **Conversational Chat** | Ask about tours like “Desert Safari” or “Burj Khalifa” — Ahmed responds with wit and warmth. |
| **Smart Price Breakdown** | Instantly calculates official vs. Ahmed’s exclusive rates and your total savings. |
| **Luxury Storytelling Style** | Responses are written in a luxury-magazine tone, blending inspiration with information. |
| **Ahmed’s Tip™ System** | Each experience includes a curated insider tip (photo hacks, timing, etiquette). |
| **Elegant Gradio UI** | Styled interface with soft gradients, refined typography, and preloaded examples. |

---

## 🧩 Tech Stack

- **Language:** Python 3.10+
- **Framework:** [Gradio](https://www.gradio.app/)
- **Libraries:** `gradio`, `datetime`, `random`
- **Interface Type:** ChatInterface
- **Deployment:** Hugging Face Spaces / Replit

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ahmedbacker/ahmed-ai-concierge.git
cd ahmed-ai-concierge
 main
