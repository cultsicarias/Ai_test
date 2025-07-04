import os
import webbrowser
import datetime
import re
from speech_engine import speak
from web_control import open_youtube_and_search 
from web_content import get_fun_fact, get_joke, get_quote, get_news_headlines, get_random_fact,get_word_of_the_day,get_quote_of_the_day, get_idiom,get_joke, get_riddle, get_cat_fact, get_did_you_know, get_today_in_history,get_top_news,get_trending_searches,get_programming_quote,get_github_trending



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

    
    if any(word in command for word in ["youtube", "watch", "play", "look up", "find"]):
        query = extract_youtube_query(command)
        if not query:
            response = "What should I search on YouTube?"
        else:
            open_youtube_and_search(query)
            response = f"Searching and playing {query} on YouTube."
        speak(response)
        return response

    
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {now}"
        speak(response)
        return response

    
    elif "open notepad" in command:
        os.system("start notepad")
        response = "Opening Notepad."
        speak(response)
        return response

   
    elif "search for" in command or "google" in command:
        query = command.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        response = f"Searching for {query}"
        speak(response)
        return response
    
    elif "news" in command or "what's happening" in command:
        response = get_news_headlines()
        speak(response)
        return response

    elif "weather" in command:
        response = get_weather("Bangalore")  
        speak(response)
        return response

    elif "horoscope" in command or "zodiac" in command:
        response = get_horoscope("aries")  
        speak(response)
        return response

    
    elif "your name" in command:
        response = "I am your custom AI assistant."
        speak(response)
        return response
    
    elif "greet me" in command:
        response = "Hello, how are you?"
        speak(response)
        return response
    
    elif "asshole" in command:
        response = "You are an asshole."
        speak(response)
        return response
    
    elif "fuck you" in command:
        response = "I'm sorry, but FUCK U"
        speak(response)
        return response
    
    elif "fuck off" in command:
        response = "I'm sorry, but FUCK OFF"
        speak(response)
        return response
    
    elif "fun fact" in command or "tell me something interesting" in command:
        response = get_fun_fact()
        speak(response)
        return response

    elif "tell me a joke" in command or "make me laugh" in command:
        response = get_joke()
        speak(response)
        return response

    elif "motivate me" in command or "inspire me" in command or "quote" in command:
        response = get_quote()
        speak(response)
        return response
    
    elif "word of the day" in command:
        response = get_word_of_the_day()
        speak(response)
        return response

    elif "idiom" in command:
        response = get_idiom()
        speak(response)
        return response

    elif "joke" in command:
        response = get_joke()
        speak(response)
        return response

    elif "riddle" in command:
        response = get_riddle()
        speak(response)
        return response

    elif "cat fact" in command:
        response = get_cat_fact()
        speak(response)
        return response

    elif "did you know" in command:
        response = get_did_you_know()
        speak(response)
        return response

    elif "today in history" in command:
        response = get_today_in_history()
        speak(response)
        return response

    elif "top news" in command or "news" in command:
        response = get_top_news()
        speak(response)
        return response

    elif "trending search" in command:
        response = get_trending_searches()
        speak(response)
        return response

    elif "programming quote" in command:
        response = get_programming_quote()
        speak(response)
        return response

    elif "trending on github" in command or "search github" in command:
        response = get_github_trending()
        speak(response)
        return response

    elif "freaky" in command:
        speak("freaky gahdhe , you are a donkey , gahdhey saalee")
        return "freaky GADHE"


    
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

   
    elif "open github" in command:
        webbrowser.open("https://github.com")
        speak("Opening GitHub.")
        return "Opening GitHub."

    elif "open reddit" in command:
        webbrowser.open("https://reddit.com")
        speak("Opening Reddit.")
        return "Opening Reddit."

    elif "shut down the computer" in command:
        speak("Shutting down. Goodbye!")
        os.system("shutdown /s /t 5")
        return "Shutting down."
    
    elif "speak" or "recite this" in command:
        speak(command)
        return command

    
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

    
    else:
        response = "Sorry, I don't know how to do that yet."
        speak(response)
        return response
