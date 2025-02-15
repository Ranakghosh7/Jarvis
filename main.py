import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

# pip install SpeechRecognition pyttsx3 requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Processes voice commands."""
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com") 
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")        
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com") 
    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")    
    elif "open pornhub" in command:
        webbrowser.open("https://pornhub.com")  
    elif "open safari" in command:
        webbrowser.open("https://safari.com")

    elif "news" in command:  
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()  # Fixed from `jason()` to `json()`
                articles = data.get('articles', [])

                if articles:
                    speak("Here are the latest news headlines:")
                    for article in articles[:5]:  # Read only top 5 headlines
                        speak(article['title'])
                else:
                    speak("No news articles found.")
            else:
                speak("Failed to fetch news.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("There was an error getting the news.")

def listen_for_command():
    """Listens for a command and processes it."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Helps reduce background noise
        print("Listening for wake word 'Jarvis'...")
        try:
            audio = recognizer.listen(source, timeout=5)
            word = recognizer.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes?")
                print("Jarvis Active... Listening for command.")
                
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                processCommand(command)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for wake word.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        listen_for_command()
