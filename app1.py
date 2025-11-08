# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 20:32:00 2025

@author: HP
"""

import streamlit as st
import cv2
import numpy as np
import requests
from datetime import datetime
from time import sleep
from PIL import Image
import speech_recognition as sr
import smtplib

# Initialize or load pre-trained models
# Assuming pre-trained models are already loaded, for example:
# emotion_model (text-based emotion analysis model)
# facial_recognition_model (for facial emotion recognition)
# speech_recognition_model (for speech-to-text and emotion analysis from speech)
# Assuming `emotion_model`, `facial_recognition_model`, and `speech_recognition_model` are already loaded

# Streamlit app layout

# 1. **Login Page**

def login_page():
    st.title("Employee Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Dummy authentication
        if username == "employee" and password == "password123":
            st.session_state.user_authenticated = True
            st.session_state.username = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# 2. **Emotion Analysis Section**
def emotion_analysis_page():
    st.title(f"Welcome {st.session_state.username}")
    
    # Option for the employee to input text, take a photo, or speak
    option = st.selectbox("Choose how you'd like to input your emotion data", ("Text", "Face", "Speech"))

    if option == "Text":
        text_input = st.text_area("Enter your text to analyze emotion")
        if text_input:
            
            # Call the pre-trained text-based emotion analysis model
            emotion = Emotiom_Analysis_Using_Text.predict_emotion(text_input)
            
            st.write(f"Detected Emotion: {emotion}")
            suggest_work_based_on_emotion(emotion)

    elif option == "Face":
        # Open webcam and analyze emotion
        run_face_recognition()

    elif option == "Speech":
        # Analyze speech input
        run_speech_recognition()

# 3. **Facial Recognition**
def run_face_recognition():
    st.write("Please allow access to your webcam...")
    stframe = st.empty()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize webcam feed
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Display image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)
        
        # For facial emotion prediction
        emotion = Emotiom_Analysis_Using_Images.pred 
        st.write(f"Detected Emotion: {emotion}")
        suggest_work_based_on_emotion(emotion)

        # Break the loop when a face is detected or stop webcam feed
        if len(faces) > 0:
            break

    cap.release()

# 4. **Speech Recognition**
def run_speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please speak now...")
        audio = r.listen(source)
        
    try:
        # Convert speech to text and analyze emotion
        speech_text = r.recognize_google(audio)
        st.write(f"Recognized Speech: {speech_text}")
        
        # Call the speech emotion analysis model
        emotion = Emotiom_Analysis_Using_Speech.predict_speech_emotion(speech_text)
        st.write(f"Detected Emotion: {emotion}")
        suggest_work_based_on_emotion(emotion)
        
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand the audio.")
    except sr.RequestError:
        st.error("Could not request results from Google Speech Recognition service.")

# 5. **Suggest Work Based on Emotion**
def suggest_work_based_on_emotion(emotion):
    if emotion == "Stressed":
        st.write("It seems like you are stressed. It's a good time to take a break.")
    elif emotion == "Neutral":
        st.write("You're doing fine! Maybe you can focus on a routine task.")
    elif emotion == "Happy" or emotion == "Inspired":
        st.write("You're in a great mood! Try engaging in some creative work.")
    else:
        st.write("You seem to be feeling overwhelmed. Take a moment to relax.")

    # Assigning tasks based on emotion (dummy task assignment)
    task = st.text_input("Task Description")
    duration = st.number_input("Task Duration (in hours)", min_value=1)
    deadline = st.date_input("Task Deadline")
    
    if st.button("Assign Task"):
        # Log task assignment (can be stored in DB)
        st.write(f"Task: {task}, Duration: {duration} hrs, Deadline: {deadline}")
        send_notification_to_team_lead()

# 6. **Send Notification to HR/Team Lead**
def send_notification_to_team_lead():
    # Example: Send an email notification to HR/Team Lead
    try:
        sender_email = "your_email@example.com"
        recipient_email = "hr@example.com"
        password = "your_password"

        # Connect to the SMTP server
        server = smtplib.SMTP_SSL("smtp.example.com", 465)
        server.login(sender_email, password)

        subject = "Employee Emotion Report"
        body = "An employee has been detected with high stress. A break or lighter task has been suggested."

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        
        st.success("Notification sent to Team Lead/HR.")
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")

# 7. **Main Application Logic**
def main():
    if "user_authenticated" not in st.session_state:
        st.session_state.user_authenticated = False

    if not st.session_state.user_authenticated:
        login_page()
    else:
        emotion_analysis_page()

if __name__ == "__main__":
    main()


