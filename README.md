# BhuvVani-Chatbot
BhuvVani processes typed or spoken messages using Flask and an NLP model to provide any information related to BHUVAN portal. Similar to Alexa, BhuvVani converts text responses into speech for an enhanced user experience. The chatbot integrates web technologies and natural language processing to facilitate efficient interactions.

# Features:

**Chatbot Interaction**: Users can interact with the chatbot by sending messages through the web interface.
**BHUVAN Portal Details**: The chatbot can provide details anything related to the BHUVAN portal based on the user's input.
**Multilingual Support**: The chatbot can respond in both English and Hindi.

# Required Python libraries:

1. nltk
2. speech_recognition
3. pyttsx3
4. keras
5. flask
6. pandas
7. pygame
8. gtts
9. pydub
10. playsound

# Installation:

1. Clone the repository:

```bash
git clone https://github.com/Dhruvrajsinh21/BhuvVani-Chatbot.git

2. Change into the project directory:

```bash
cd BhuvVani-Chatbot

3. Usage:
Run the Flask app:

```bash
python app.py
Open a web browser and go to http://localhost:5000/ to interact with the chatbot.

Enter messages in the chat input and view the responses from the chatbot.

4. Configuration:
Model and Data Files:

├── model.h5               # Keras model file for chatbot.
├── data.json              # JSON file containing intents for chatbot training.
├── texts.pkl              # Pickle file containing preprocessed text data.
└── labels.pkl             # Pickle file containing chatbot labels.

Aadhar Center Data:

├── Aadhar-Center-List.xls.xlsx   # Excel file containing Aadhar center details.


 
![BhuvVani](https://github.com/Dhruvrajsinh21/BhuvVani-Chatbot/assets/115185535/b0d92d1f-3a63-4a58-991c-041ba8b6248d)
