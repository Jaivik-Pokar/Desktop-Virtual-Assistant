# Library
import pyttsx3  # AI to speak
import datetime
import speech_recognition as sr  # Speech to text
import wikipedia  # Wikipedia search
import os  # Opening local files
import webbrowser  # Web browsing
import random  # For random voice selection
import openai

# Importing the voice for our AI
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
selected_voice = random.choice([0, 1])
engine.setProperty('voice', voices[selected_voice].id)
openai.api_key = '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'

# Greeting function
def speak(audio):
    try: 
        engine.say(audio) 
        engine.runAndWait() 
    except Exception as e: 
        print(f"Error in speak function: {str(e)}")

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("It is a fine morning, sir!")
    elif 12 <= hour < 18:
        speak("Hope you had your brunch. Good Afternoon, sir!")
    else:
        speak("The wind is lovely. Good Evening, sir!")

    speak("Hello! How are you? I am your personal AI Assistant. How can I be of service?")

# Command function
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("I could not understand. Please speak again.")
        return "None"
    return query

# Main tasks
if __name__ == "__main__":
    greet()

    while True:
        query = command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'chat gpt' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            try:
        # Use OpenAI API to get information
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=f"Tell me about {query}",
                    max_tokens=150
                )
                result = response.choices[0].text.strip()
                speak(f"According to OpenAI, {result}")
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that topic.")
                print(f"Error: {str(e)}")
                
        # Working Instagram
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        
        # Working Youtube
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        # Working Google
        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")
        
        # Working Kaggle
        elif 'open kaggle' in query:
            webbrowser.open("https://www.kaggle.com/")
            
        # Working Weather
        elif 'the weather' in query:
            webbrowser.open("https://www.google.com/search?q=weather")
        
        # Working Naukri .com
        elif 'open naukri.com' in query:
            webbrowser.open("https://www.naukri.com/mnjuser/homepage")
        
        # Working LinkedIn
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/jaivik-pokar-98a334247/")        
        
        # Working Cricket score
        elif 'cricket score' in query:
            webbrowser.open("https://www.cricbuzz.com/cricket-match/live-scores")
        
        # Working Music
        elif 'play music' in query or 'open spotify' in query:
            music_dir = 'https://open.spotify.com/playlist/0ffnLxCftwLzmXDO7DJEXc?si=5a076c3405f54243'
            webbrowser.open(music_dir)
        
        # Working Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Time: {strTime}')
            speak(f'Sir, the time is {strTime}')
            
        # Working Word Document
        elif 'open word document' in query:
            worddoc_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            # os.startfile(worddoc_path)
            try:
                os.startfile(worddoc_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find Microsoft Word on your system.")

        # Working PPT
        elif 'open powerpoint' in query:
            ppt_path = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            # os.startfile(ppt_path)
            try:
                os.startfile(ppt_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find Microsoft PowerPoint on your system.")

        # Working VS code
        elif 'open vs code' in query:
            vscode_path = r"C:\Users\Jaivik\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            # os.startfile(vscode_path)
            try:
                os.startfile(vscode_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find Visual Studio Code on your system.")

        # Working Gmail
        elif 'open gmail' in query:
            gmail_url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
            webbrowser.open(gmail_url)
        
        # Working Bye
        elif 'thank you' in query or 'bye' in query or 'tata' in query or 'thank' in query:
            speak("Goodbye! Take care!")
            break  # Exit the loop
    print("AI Assistant has stopped.")  