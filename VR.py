import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import datetime
import webbrowser

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text to speech engine
engine = pyttsx3.init()

def speak(text):
    """
    Function to speak the given text
    """
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Function to listen to the user's voice command
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def greet():
    """
    Function to greet the user
    """
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you today?")

def get_time():
    """
    Function to get the current time
    """
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def get_date():
    """
    Function to get the current date
    """
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")

def search_web(query):
    """
    Function to search the web based on user query
    """
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

def main():
    """
    Main function to execute the voice assistant
    """
    greet()

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello there!")

        elif "time" in query:
            get_time()

        elif "date" in query:
            get_date()

        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            search_web(search_query)

        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()