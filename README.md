🌿 WellMind Connect – AI-Powered Youth Mental Wellness Companion

🧠 Overview

WellMind Connect is an AI-powered, confidential, and empathetic mental wellness platform designed to support youth in expressing emotions safely, tracking their moods, and accessing real-time help when needed.

Our goal is to reduce the stigma surrounding mental health by offering an AI companion that understands, guides, and connects users to verified helplines through a secure, stigma-free digital experience.

💡 Key Features

Feature - Description

🤖 Empathetic AI Chatbot (Gemini-based)-Provides multilingual, emotion-aware conversations for daily check-ins and guidance.

😊 Mood Tracking & Journaling-Allows users to record mood entries using emojis/text and view emotional trends.

Crisis Detection & Helpline Integration-Detects distress signals and connects users to verified helplines in real time.

💬 Personalized Coping Strategies-Suggests wellness tips, relaxation techniques, or study motivation based on mood.

🌐 Multilingual Accessibility-Supports English and Indian regional languages for inclusivity.

🔐 Confidential & Secure-Built with Firebase authentication and Google Cloud to ensure privacy.

🚀 Tech Stack

Layer - Technologies
Frontend-Streamlit / React / Flutter

Backend-Python (Flask / FastAPI)

AI/ML Models-Google Gemini API (chat), Vertex AI (mood analysis)

Database-Google Cloud Firestore / Cloud SQL

Authentication-Firebase Authentication

Deployment-Google Cloud Run / Firebase Hosting

Notifications-Firebase Cloud Messaging

Storage-Google Cloud Storage

🧩 Architecture Diagram

Start / Login
      │   
      ▼
Chat with AI (Gemini)
      │
      
      ├──► Mood Tracking  
      
      │         │   
      
      │         └──► Personalized Tips (via Vertex AI)
      
      │
      ├──► Crisis Detected?
      
      │       ├── Yes → Connect to Helpline
      
      │       └── No  → Continue Chat
      
      │
 End / Logout


USP – What Makes It Unique

Confidential & stigma-free space for youth mental health.

Emotionally intelligent, multilingual chatbot powered by Google Gemini.

Real-time crisis detection with helpline integration.

Personalized wellness plans through AI-driven insights.

Built on a secure and scalable Google Cloud architecture.

⚙️ How to Run the Prototype Locally

1️⃣ Clone the repository

git clone https://github.com/Ashwini-12a-coder/wellmind-connect-prototype.git

cd wellmind-connect-prototype

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the app

python app.py

4️⃣ Open in browser

http://localhost:8501


(If using Streamlit, the app will auto-launch in your browser.)

🧪 Prototype Features (Demo Version)

✅ AI Chatbot (Google Gemini API)

✅ Mood Tracking & Journaling

✅ Crisis Detection & Alert Simulation


📂 Project Structure

wellmind-connect-prototype/

│
├── app.py      # Main application file

├── requirements.txt            # Python dependencies

├── mood_history.json           # Sample mood tracking data

├── README.md                   # Project documentation

└── assets/                     # (optional) images, UI files


🌱 Future Enhancements

AI-based emotion recognition from text and voice.

Community support groups & gamified engagement.

Integration with meditation, journaling, and goal-tracking modules.

Mental health awareness resources curated for youth.
