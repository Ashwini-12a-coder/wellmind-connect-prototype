import streamlit as st
import openai
import json
from datetime import datetime
# from googletrans import Translator  # Optional, remove if not needed

# ---------------- CONFIG ----------------
st.set_page_config(page_title="WellMind Connect", page_icon="🧠", layout="centered")
st.title("🧠 WellMind Connect")
st.subheader("Your AI-Powered Youth Mental Wellness Companion")

# OpenAI API key (replace with your own key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# File to store mood history
MOOD_FILE = "mood_history.json"

# Initialize translator
# translator = Translator()

# ---------------- UTILITY FUNCTIONS ----------------
def save_mood(date, mood, tip):
    try:
        with open(MOOD_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append({"date": date, "mood": mood, "tip": tip})
    with open(MOOD_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly, empathetic mental wellness assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )
        reply = response['choices'][0]['message']['content']
        return reply
    except Exception as e:
        return "I’m here to listen. Tell me more about how you feel."

# ---------------- CHATBOT FEATURE ----------------
st.header("💬 Chatbot for Emotional Support")
user_input = st.text_input("How are you feeling today?")

if user_input:
    # Crisis detection first
    if any(word in user_input.lower() for word in ["suicide", "kill myself", "self-harm"]):
        st.warning("⚠️ If you are in crisis, please contact a helpline immediately: 022-2754-6669 (India)")
    else:
        # Generate AI response
        ai_reply = generate_ai_response(user_input)
        st.write(ai_reply)

# ---------------- MOOD TRACKER FEATURE ----------------
st.header("📊 Mood Tracker")
mood = st.selectbox("Select your current mood:", ["😀 Happy", "😔 Sad", "😟 Stressed", "😡 Angry"])
tips = {
    "😀 Happy": "Keep up the positivity! Share your joy with friends.",
    "😔 Sad": "It’s okay to feel sad. Try journaling or listening to soothing music.",
    "😟 Stressed": "Take a short walk, do deep breathing, or listen to calming music.",
    "😡 Angry": "Pause, take deep breaths, and try to relax before reacting."
}

if st.button("Save Mood"):
    date_now = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    tip = tips[mood]
    save_mood(date_now, mood, tip)
    st.success(f"Mood '{mood}' saved with tip: {tip}")

# Optionally show mood history
if st.checkbox("Show Mood History"):
    try:
        with open(MOOD_FILE, "r") as f:
            history = json.load(f)
            for entry in reversed(history):
                st.write(f"{entry['date']} - {entry['mood']} → {entry['tip']}")
    except:
        st.info("No mood history found.")

# ---------------- CRISIS SUPPORT ----------------
st.header("🚨 Crisis Support")
st.markdown(
    "- **National Helpline (India): 022-2754-6669**\n"
    "- **International Hotline (Suicide Prevention): +1-800-273-8255**\n"
)
st.markdown("**Remember:** You are not alone. Seeking help is a sign of strength! 💙")

# ---------------- MULTILINGUAL SUPPORT (Optional) ----------------
# st.header("🌐 Translate Your Mood Tips (Optional)")
# selected_lang = st.selectbox("Select Language:", ["English", "Hindi", "Tamil", "Telugu"])
# if st.button("Translate Tips"):
#     translated = {m: translator.translate(t, dest=selected_lang[:2].lower()).text for m, t in tips.items()}
#     for m, t in translated.items():
#         st.write(f"{m} → {t}")
