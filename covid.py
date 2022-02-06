from itertools import count
from bs4 import BeautifulSoup
import requests
import pyttsx3
import speech_recognition as sr


print("Wait...")       

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('voice', voices[0].id)
# print(voices[1].id)
engineio.setProperty('rate', 115)
# engine.say("Hello, How are you ?")
engineio.runAndWait()

def speak(str):
    engineio.say(str)
    engineio.runAndWait()
    
#scraping the covid site
html_text = requests.get('http://codewani.pythonanywhere.com/').text
soup = BeautifulSoup(html_text, 'lxml')
dock_elements = soup.find_all('h5', class_ = 'card-text')
# print(dock_elements)
count = 0
for i in dock_elements:
    count += 1
    if count == 1:
        totalcases = i.text
    if count == 2:
        totalrecoveries = i.text
    if count == 3:
        activecases = i.text
    if count == 4:
        deaths = i.text
    if count == 5:
        tests = i.text
    if count == 6:
        todaycases = i.text
    if count == 7:
        todayrecoveries = i.text
    if count == 8:
        todaydeaths = i.text

# the below print statement waits for everything to run before microphone is activated
print('Now speak')

r = sr.Recognizer()

with sr.Microphone() as source:
    # r.adjust_for_ambient_noise(source)
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    words = text.split(" ")
    if  "total" in words and "cases" in words  and "today" not in words:
        speak(f"The Total Number of Cases in Zambia is {totalcases} ")
    elif ("total" or "cumulative" in words) and  "deaths" in words and "today" not in words:
        speak(f"The Total Number of Deaths in Zambia is {deaths}")
    elif ("total" or "cumulative" in words) and "recoveries" in words and "today" not in words:
        speak(f"The Total Number of Recoveries in Zambia is {totalrecoveries}")
    elif "active" in words and "cases" in words: 
        speak(f"The Total Number of Active Cases in Zambia is {activecases}")
    elif "cases" in words and  "today" in words:
        speak(f"The Number of Cases Recorded today in Zambia is {todaycases}")
    elif "tests" in words and  "today" in words:
        speak(f"The Number of  Tests Conducted today in Zambia is {tests}")
    elif "recoveries" in words and  "today" in words:
        speak(f"The Number of Recoveries Recorded today in Zambia is {todayrecoveries}")
    elif "deaths" in words and  "today" in words:
        speak(f"The Number of Deaths Recorded today in Zambia is {todaydeaths}")
    
    