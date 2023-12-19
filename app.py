import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
import speech_recognition as sr
import pyttsx3
import pyttsx4
from keras.models import load_model
import json
import random
from flask import Flask, render_template, request, make_response
import pandas as pd
import os
import pygame
import threading 
from pyttsx3.drivers import sapi5
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from playsound import playsound

app = Flask(__name__)
app.static_folder = 'static'

model = load_model('model.h5')
intents = json.loads(open('data.json').read())
words = pickle.load(open('texts.pkl', 'rb'))
classes = pickle.load(open('labels.pkl', 'rb'))

aadhar_centers_df = pd.read_excel('Aadhar-Center-List.xls.xlsx')

audio_file_path = 'sound.mp3'

def speak(text):
    engine = pyttsx3.init()
    print(text)
    if text=='Hello, how can I help you?':
        text = 'नमस्ते, मैं आपकी कैसे सहायता कर सकती हूँ?'
        text_to_speech_hindi(text)
    else:
        engine.say(text)
        engine.runAndWait()
        
def text_to_speech_hindi(text):
    try:
        tts = gTTS(text=text, lang='hi', slow=False)
        tts.save("output.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()
    except Exception as e:
        print(f"Error in text_to_speech_hindi: {e}")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [WordNetLemmatizer().lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def filter_aadhar_centers(sentence):
    filtered_df = aadhar_centers_df[aadhar_centers_df['District'] == sentence]
    print(filtered_df)
    print(sentence)
    return filtered_df

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            speak(result)
            break
    return result

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents) 

    # Use threading to play the notification sound simultaneously
    threading.Thread(target=play_audio, args=(audio_file_path,)).start()

    return res

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    output = chatbot_response(userText)

    if "Aadhar center details" in output:
        userText = userText.replace(".", "")
        userText = userText.capitalize()
        filtered_centers = filter_aadhar_centers(userText)

        if not filtered_centers.empty:

            # Create an HTML table from the CSV data
            csv_content_table = filtered_centers.to_html(index=False)

            # Include HTML table in the chatbot response
            response_text = f"Here are the Aadhar center details:\n\n{csv_content_table}"

            # Serve the CSV file for download
            try:
                # Set the response content type to CSV
                response = make_response(csv_content_table) 
                response.headers["Content-Type"] = "text/html"
                response.headers["Content-Disposition"] = "attachment; filename=filtered_aadhar_centers.xlsx"
                response_content_str = str(response.data, response.charset)
                url = "https://bhuvan-app3.nrsc.gov.in/aadhaar/"
                url=f'<a href="{url}" target="_blank">{url}</a>'
                response_content_with_url = f"{response_content_str}<br><br>For more information, visit:<br> {url}"
                # Set the Content-Disposition header to trigger download
                return response_content_with_url
            except Exception as e:
                print(f"Error serving CSV file: {str(e)}")
                return "Error serving CSV file."

        else:
            return "No Aadhar center details found for the given input."

    return output

if __name__ == "__main__":
    app.run(debug=True)