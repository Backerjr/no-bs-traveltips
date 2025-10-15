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