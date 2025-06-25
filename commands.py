import os
import webbrowser
import datetime
import re
from speech_engine import speak
from web_control import open_youtube_and_search  # Using Selenium+JS version

# 🧠 Extract YouTube search query from conversational commands
def extract_youtube_query(command):
    command = command.lower()
    filler_phrases = [
        "can you", "could you", "please", "for me", "i want to", "i wanna", "i'd like to",
        "hey", "buddy", "ai", "assistant", "search youtube for", "play on youtube",
        "find on youtube", "look up on youtube", "youtube search", "i want to watch",
        "search", "watch", "show me", "look for"
    ]
    for phrase in filler_phrases:
        command = command.replace(phrase, "")
    return re.sub(r"[^a-zA-Z0-9\s]", "", command).strip()

def process_command(command):
    command = command.lower()

    # 🎯 Smart YouTube Intent Detection
    if any(word in command for word in ["youtube", "watch", "play", "look up", "find"]):
        query = extract_youtube_query(command)
        if not query:
            response = "What should I search on YouTube?"
        else:
            open_youtube_and_search(query)
            response = f"Searching and playing {query} on YouTube."
        speak(response)
        return response

    # 🕐 Time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {now}"
        speak(response)
        return response

    # 📓 Notepad
    elif "open notepad" in command:
        os.system("start notepad")
        response = "Opening Notepad."
        speak(response)
        return response

    # 🌐 Web Search
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        response = f"Searching for {query}"
        speak(response)
        return response

    # 🧠 Identity
    elif "your name" in command:
        response = "I am your custom AI assistant."
        speak(response)
        return response

    # 🌞 Greetings
    elif "good morning" in command or "good night" in command:
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            response = "Good morning! Hope you have a productive day."
        elif 12 <= hour < 18:
            response = "Good afternoon! Keep up the good work."
        elif 18 <= hour < 22:
            response = "Good evening! You did great today."
        else:
            response = "It's pretty late, you should get some rest!"
        speak(response)
        return response

    # 🌐 Websites
    elif "open github" in command:
        webbrowser.open("https://github.com")
        speak("Opening GitHub.")
        return "Opening GitHub."

    elif "open reddit" in command:
        webbrowser.open("https://reddit.com")
        speak("Opening Reddit.")
        return "Opening Reddit."

    # 🔻 Shutdown
    elif "shut down the computer" in command:
        speak("Shutting down. Goodbye!")
        os.system("shutdown /s /t 5")
        return "Shutting down."

    # 🆘 Help
    elif "help" in command:
        response = (
            "Here’s what I can do:\n"
            "- Play videos on YouTube\n"
            "- Search Google\n"
            "- Tell you the time\n"
            "- Open apps and websites\n"
            "- Greet you\n"
            "- Shut down the computer"
        )
        speak(response)
        return response

    # ❓ Fallback
    else:
        response = "Sorry, I don't know how to do that yet."
        speak(response)
        return response
