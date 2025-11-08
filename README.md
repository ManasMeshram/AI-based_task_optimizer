# AI-based_task_optimizer

# 🤖 Amdox: AI-Powered Task Optimizer

**Real-time emotion detection and mood-based task recommendations**
A prototype designed to enhance productivity and well-being by monitoring employee emotions through text and webcam inputs, then suggesting tasks that align with their emotional state.

---

## 🚀 **Overview**

Amdox leverages **AI-powered emotion recognition** to help teams and individuals stay balanced and productive. It detects emotions from text, webcam, or manual selection, then provides personalized task recommendations and mood analytics — all while maintaining user privacy.

---

## 🌟 **Key Features**

1. **🧠 Real-Time Emotion Detection**

   * Analyze emotions from **text input** or **webcam video**.
   * Supports moods like *Angry, Sad, Neutral, Happy, Surprised, Fear, Disgust, Excited, Calm.*

2. **🎛 Manual Emotion Selection**

   * Users can manually select their current mood from a dropdown.
   * Serves as an alternative to AI-based detection.

3. **🗂 Task Recommendation System**

   * Suggests context-appropriate tasks based on emotion.
   * Example:
     `Detected: Sad → Suggested Tasks: Light documentation, wellness break.`

4. **📊 Historical Mood Tracking**

   * Logs emotional data in `data/mood_history.csv`.
   * Enables mood trend analysis over time.

5. **👥 Team Mood Analytics**

   * Aggregates emotional data to identify overall team morale and productivity patterns.

6. **⚠️ Stress Management Alerts**

   * Detects prolonged negative emotions and alerts HR or managers proactively.

7. **🔒 Data Privacy**

   * Stores only anonymized data: timestamp, source, emotion, and score.
   * No personal identifiers are collected.

---

## 🧩 **Input Modes**

| Mode                       | Description                                           |
| -------------------------  | ----------------------------------------------------- |
| 📝 **Text Input**          | Type sentences like “I’m feeling exhausted but okay.” |
| 🎥  **Webcam (Real-Time)** | Detects facial expressions from live video feed.      |
| 🎚  **Manual Selection**    | Choose your mood manually from a predefined list.     |

---

## ⚙️ **Quick Start**

### 1. Clone the repository

### 2. Create a virtual environment & install dependencies

### 3. Run the Streamlit app

## 🧠 **Data Storage**

## 🔮 **Future Enhancements**

1. **🗣️ Voice Sentiment Analysis**

   * Integrate speech-based emotion detection from tone and pitch using `SpeechRecognition` and `OpenAI Whisper`.

2. **📈 Intelligent Mood Dashboard**

   * Interactive dashboards to visualize personal and team emotional trends using Plotly or Streamlit Charts.

3. **🧩 Personalized AI Assistant**

   * Introduce an in-app chatbot that recommends personalized well-being or productivity strategies based on your current mood.

4. **🌍 Multi-Language Support**

   * Expand emotion detection for multilingual input using Hugging Face multilingual transformer models.

5. **🧘 Wellness Integration**

   * Sync with meditation, fitness, or focus apps (e.g., Calm, Headspace, Fitbit) for holistic wellness recommendations.

6. **🔒 Federated Learning for Privacy**

   * Implement decentralized model training where emotion data never leaves the user’s device.

---

## 📜 **License**

This project is licensed under the **MIT License** — free for personal and commercial use with attribution.

---

## 🙌 **Acknowledgements**

*  Emotion Analysis Using Text — Emotion classification models
*  Emotion Analysis Using Images — Facial Expression Recognition model
*  
* [📊 Streamlit](https://streamlit.io/) — Interactive web app framework

---

## 👩‍💻 **Author**

**Manas Meshram**
Computer Science Student | AI & Data Science Enthusiast
Email - meshrammanas4@gamil.com
---
