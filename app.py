#remember the code runs on github+streamlit. You can save you code here for future reference.
#Reuse your code from Task 4 to make it into a Streamlit app. Make sure you make the following changes:

#Add gtts to requirements.txt file on github (see Class05 slides if you have no idea what i am talking about)
#Replace input() with st.text_input(...)
#Replace ipd.display(ipd.Audio(...) with st.audio(...)

import streamlit as st
from googletrans import Translator
from gtts import gTTS

# It asks the user to type in some text
st.write("Give me some text you want me to translate in English and read for you:")
user_text = st.text_input("Put your text here")
#if user_text =! " " then do smth, otherwise do
# It then converts that text in a certain langauge
translator = Translator()
text_to_translate = translator.translate(text=user_text, dest='en') 
st.write("Your translated text is:", text_to_translate.text)
text_to_speech = text_to_translate.text

# it converts the translated text to speech.
tts=gTTS(text=text_to_speech, lang='en')
tts.save('audio.mp3')

st.write("Your translated text would sound like this in English:")
audio_file = open('audio.mp3', "rb")
st.audio(data=audio_file, format="audio/mp3", start_time=0)
st.download_button(label="Download audio file", data=audio_file, file_name='audio.mp3',mime='audio/mp3')
