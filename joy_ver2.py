# Find comment called- UPDATE from ver 2.0, below. Rest of 
# the code above that is similar to ver 1.0
# Features added to the second version:
# 1. 1 line search result even without opening any search browser by Wolframalpha API.
# 2. Weather Updates
# 3. Any calculation can be performed by our assistant. Using Wolframalpha API
# 3. Jokes telling
# 4. Shutdown, restart, logout features
# 5. CPU & Battery info using psutil module
# 6. Screenshot feature
# Thats it. Stay tuned for joy_ver3 for more cool features.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib
from selenium import webdriver
import random
import wolf_alpha
import pyautogui_functions
import pyjokes
import psutil

engine = pyttsx3.init('sapi5')
# We set the voice( male/female) here
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# This is our main method by which we will take voice input/ command
# from our user.
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # 3s pause
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# This method will tell us current time
def time():
    Time = datetime.datetime.now().strftime('%H:%M') # You can also add seconds simply adding ':%S'
    speak("Hello Sir ,now the time is " + Time)

# Method which helps our assistant to let us know the current date(dd-mm-yyyy)
def date():
    date = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    speak("Today's date is,")
    speak(date)
    speak(month)
    speak(year)

# At the opening of the program it will wish us according to the day's part
def wishMe():
    wish = ''
    t = datetime.datetime.now().hour
    if t >= 6 and t < 12:
        wish = 'Good morning'
    elif t >= 12 and t < 18:
        wish = 'Good afternoon'
    elif t >= 18 and t < 24:
        wish = 'Good Evening'
    else:
        wish = 'Good Night'
    speak(wish + ",Sir, I am Joy. How can I help you?")

# Most exciting part. By this method we automate the send email functionality of Joy, our AI assistant
def send_email(to,content):
    server_setup = smtplib.SMTP("smtp.gmail.com", 587)
    server_setup.ehlo()
    server_setup.starttls()
    server_setup.login('pywithjoy@gmail.com','Joyjoy570*')
    server_setup.sendmail('pywithjoy@gmail.com', to, content)
    server_setup.close()

# After take command, the most important and main method of our entire code
# It will process the query you gave according to your desire
def process(query):
    # By this you can get wiki serach results even without opening real wikipedia
    if 'wikipedia' in query:
        speak("Searching wikipedia.....")
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=2)
        # You can increase or decrease the value of sentences parameter.
        # Sentences parameter defines how many lines of results you want.
        print(result)
        speak("According to search..")
        speak(result) # Your AI assistant, Joy will read the search result for you

    # Website opening through webbrowser module
    elif 'open youtube' in query:
        speak("Opening youtube....")
        webbrowser.get("windows-default").open('youtube.com')

    # You can also tell specifically what you actually search on youtube. ex: search youtube wasim akram
    elif 'search youtube' in query:
        red_words_yt = ['in', 'youtube', 'on', 'find', 'search youtube', 'search']#we'll not include this word into search bar
        query = query.split()
        green_word_yt = [word for word in query if word.lower() not in red_words_yt] # We'll only include what you serched
        search_key = ''.join(green_word_yt)
        speak("Opening in youtube")
        webbrowser.get("windows-default").open("https://www.youtube.com/results?search_query= "+search_key)

    elif 'news' in query:
        speak("Opening newspaper")
        webbrowser.get("windows-default").open('https://www.prothomalo.com/')
    # command example: search google shakib al hasan(Say anything but include
    # search google before the item you want to search for)
    elif 'search google' in query:
        red_word_gle = ['search', 'google', 'in', 'find', 'search google']
        query = query.split()
        green_word_gle = [word for word in query if word.lower() not in red_word_gle]
        search_key_gle = ''.join(green_word_gle)
        speak("Searching google")
        webbrowser.get("windows-default").open("https://google.com/search?q= "+ search_key_gle)

    elif 'open google' in query:
        speak("opening google ")
        webbrowser.get("windows-default").open('https://www.google.com')

    # Application openning/clossing from your machine

    elif 'file' in query:
        speak("Opening file explorer..")
        file_explorer = "C:\\Users\\JSP-NogorIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.lnk"
        os.startfile(file_explorer)
    elif 'open chrome' in query:
        speak("Opening google chrome..")
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)

    elif 'close chrome' in query:
        speak("closing Chrome browser")
       # os.system("Taskkill /IM chrome.exe /F")
        os.system("TASKKILL /F /IM chrome.exe")
    # Microsoft Office openning/clossing
    elif 'open word' in query or "microsoft word" in query:
        speak("Opening Microsoft word")
        word_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        os.startfile(word_path)
    elif 'close word' in query:
        speak("closing Microsoft word")
        os.system("TASKKILL /IM WINWORD.EXE")
    elif 'open powerpoint' in query or "power point" in query:
        speak("Opening Microsoft Powerpoint")
        ppt_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        os.startfile(ppt_path)
    elif 'close powerpoint' in query or 'close power point' in query:
        speak("closing Microsoft Powerpoint")
        os.system("TASKKILL /IM POWERPNT.EXE")
    elif 'open excel' in query or 'microsoft excel' in query:
        speak("Opening Microsoft excel")
        xl_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        os.startfile(xl_path)
    elif 'close excel' in query or 'close xl' in query:
        speak("closing Microsoft Excel")
        os.system("TASKKILL /IM EXCEL.EXE")
    # send email query
    elif 'send email' in query or 'send an email'in query or 'email' in query:
        try:
            speak('Sure, What should I say?')
            email_body = takeCommand()
            speak('Got it. Please write the receiver email address ')
            # to = input("Enter the receiver email: ")
            to = pyautogui_functions.email_taking_prompt()
            send_email(to, email_body)
            speak("Succesfully send your mail.")
        except Exception:
            speak('Sorry, I failed to sent the email...Try again please.')
    # Play music
    elif 'play music' in query or 'gana' in query or 'gun' in query:
        speak("Playing Music for you")
        music_path = "C:\\Users\\JSP-NogorIT\\Music"
        music = os.listdir(music_path)
        os.startfile(os.path.join(music_path, music[random.randint(0,118)]))
    #FAQ
    # Time
    elif 'time' in query or 'somoy' in query:
        time()
    # Date
    elif 'what is the date' in query or 'tarikh' in query or "today's date" in query:
        date()
    elif 'coronavirus' in query or 'corona' in query or 'corona virus' in query:
        webbrowser.get("windows-default").open("http://covid19tracker.gov.bd/")
    # Want to who is Joy? He is ready for his introduction...
    elif 'introduce yourself' in query or 'tell me about yourself' in query or 'who are you' in query:
        introduction = ''' I am Joy, your personal AI assistant.
                               I am created by,  Maruf Islam
                               I am ready to make your life easier.
                               Tell me what you want to do?
                               '''
        speak(introduction)
    elif 'thank you' in query:
        speak("Its my pleasure. What else you need")
    # Its time to leave? He will say goodbye to you in a nice way.
    elif 'quit' in query or 'exit' in query or 'goodbye' in query or 'bye' in query or 'sleep' in query or 'stop' in query:
        speak("Goodbye...It was a great time with you.")
        quit()

    #---------------------------------------------------------------------------------------------
    # UPDATE from ver 2.0
    # WolframAlpha integration.
    # Find wolf_alpha.py in this repository for the methods we used
    elif 'calculate' in query or 'solve' in query :
        speak("Give me sometime to calculate..")
        wolf_alpha.math_solver(query)
    elif 'weather' in query or 'forecast' in query:
        speak('Generating.. weather information')
        wolf_alpha.weather(query)
    elif 'what' in query or 'who' in query:
        speak("Let me find it out:")
        wolf_alpha.search(query)
    # Screen capture/shot
    elif 'screenshot' in query or 'screen shot' in query or 'snap' in query or 'snapshot' in query:
        speak("Taking screenshot")
        pyautogui_functions.take_scrnshot()
        speak("Successfully taken. Find it in the selected folder")
    # Jokes. Yeah 'Joy' isn't that much boring'
    elif 'jokes' in query or 'joke' in query or 'fun' in query:
        speak("Ok buddy.. let me remember.")
        jokes = pyjokes.get_joke()
        print(jokes)
        speak('Yeah got it, listen, '+jokes)
    # CPU & Battery info
    elif 'cpu' in query or 'cpu info' in query:
        cpu_usage = str(psutil.cpu_percent())
        speak("Your cpu usage is,"+ cpu_usage)
    # Battery info for laptop
    elif 'battery' in query or 'charge' in query:
        battery = psutil.sensors_battery()
        speak("Your remaining power is" + battery.percent)
    # Basic control
    elif 'sign out' in query or 'logout' in query or 'signout' in query:
        speak("Signing out..")
        os.system('shutdown -l')
    elif 'restart' in query:
        speak("Restarting your machine")
        os.system('shutdown /r /t l')
    elif 'shutdown' in query or 'power off' in query or 'shutting down' in query:
        speak('Shutting down')
        os.system('shutdown /s /t l')


if __name__ == '__main__':
    wishMe()
    while True :
        query = takeCommand().lower()
        process(query)





