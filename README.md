# BhuvVani-Chatbot
BhuvVani processes typed or spoken messages using Flask and an NLP model to provide any information related to BHUVAN portal. Similar to Alexa, BhuvVani converts text responses into speech for an enhanced user experience. The chatbot integrates web technologies and natural language processing to facilitate efficient interactions.

Features
Chatbot Interaction: Users can interact with the chatbot by sending messages through the web interface.

BHUVAN Portal Details: The chatbot can provide details anything related to the BHUVAN portal based on the user's input.

Multilingual Support: The chatbot can respond in both English and Hindi.

Requirements:

Make sure you have the following dependencies installed before running the chatbot:

Python 3.x
Required Python libraries (install using pip install -r requirements.txt):
nltk
speech_recognition
pyttsx3
keras
flask
pandas
pygame
gtts
pydub
playsound

Installation

Clone the repository:

bash
Copy code
git clone https://github.com/Dhruvrajsinh21/BhuvVani-Chatbot.git
Change into the project directory:

bash
Copy code
cd BhuvVani-Chatbot
Install the required dependencies:

Usage
Run the Flask app:

bash
Copy code
python app.py
Open a web browser and go to http://localhost:5000/ to interact with the chatbot.

Enter messages in the chat input and view the responses from the chatbot.

Configuration
Model and Data Files:

model.h5: Keras model file for chatbot.
data.json: JSON file containing intents for chatbot training.
texts.pkl: Pickle file containing preprocessed text data.
labels.pkl: Pickle file containing chatbot labels.
Aadhar Center Data:

Aadhar-Center-List.xls.xlsx: Excel file containing Aadhar center details.
 
![BhuvVani](https://github.com/Dhruvrajsinh21/BhuvVani-Chatbot/assets/115185535/b0d92d1f-3a63-4a58-991c-041ba8b6248d)
