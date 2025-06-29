import requests
from bs4 import BeautifulSoup
import random

headers = {'User-Agent': 'Mozilla/5.0'}

# 🧠 Fun Fact
def get_fun_fact():
    try:
        res = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
        soup = BeautifulSoup(res.text, 'html.parser')
        facts = soup.select("ul li")
        return random.choice(facts).text.strip()
    except:
        return "Couldn't fetch a fun fact right now!"

# 😂 Joke
def get_joke():
    try:
        res = requests.get("https://upjoke.com/")
        soup = BeautifulSoup(res.text, 'html.parser')
        jokes = soup.select(".joke-text")
        return random.choice(jokes).text.strip()
    except:
        return "Oops! I can't find a joke right now."

# 💪 Motivation
def get_quote():
    try:
        res = requests.get("https://www.keepinspiring.me/positive-inspirational-life-quotes/")
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.select("blockquote p")
        return random.choice(quotes).text.strip()
    except:
        return "You're doing great! Keep going!"

# ------------------ Language & Quotes ------------------
def get_random_fact():
    res = requests.get("https://www.thefactsite.com/1000-interesting-facts/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    facts = soup.select(".post-content li")
    return random.choice(facts).text.strip() if facts else "Couldn't fetch a fact."

def get_word_of_the_day():
    res = requests.get("https://www.merriam-webster.com/word-of-the-day", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    word = soup.find("h1")
    definition = soup.find("div", {"class": "wod-definition-container"})
    if word and definition:
        return f"{word.text.strip()}: {definition.text.strip()}"
    return "Couldn't fetch word of the day."

def get_quote_of_the_day():
    res = requests.get("https://www.brainyquote.com/quote_of_the_day", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    quote = soup.find("img", {"class": "p-qotd"})
    return quote["alt"] if quote else "Couldn't fetch a quote."

def get_idiom():
    res = requests.get("https://www.englishclub.com/ref/Idioms/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    idioms = soup.select("#page li a")
    return random.choice(idioms).text.strip() if idioms else "No idiom found."

# ------------------ Fun & Entertainment ------------------
def get_joke():
    res = requests.get("https://upjoke.com/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    joke = soup.select_one(".joke-text")
    return joke.text.strip() if joke else "Couldn't fetch a joke."

def get_riddle():
    res = requests.get("https://www.riddles.com/riddle-of-the-day", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    riddle = soup.find("h2")
    return riddle.text.strip() if riddle else "Couldn't fetch a riddle."

def get_cat_fact():
    res = requests.get("https://www.thefactsite.com/100-cat-facts/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    facts = soup.select(".post-content li")
    return random.choice(facts).text.strip() if facts else "Couldn't fetch cat fact."

def get_did_you_know():
    res = requests.get("https://didyouknowfacts.com/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    posts = soup.select(".post-title")
    return random.choice(posts).text.strip() if posts else "Couldn't fetch trivia."

# ------------------ World & News ------------------
def get_today_in_history():
    res = requests.get("https://www.onthisday.com/", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    events = soup.select(".event")
    return random.choice(events).text.strip() if events else "Couldn't fetch history event."

def get_news_headlines():
    res = requests.get("https://www.bbc.com/news", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    headlines = soup.select(".gs-c-promo-heading__title")
    top = [h.text.strip() for h in headlines[:3]]
    return "\n".join(top) if top else "Couldn't fetch news."

def get_top_news():
    res = requests.get("https://www.bbc.com/news", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    headlines = soup.select(".gs-c-promo-heading__title")
    top = [h.text.strip() for h in headlines[:3]]
    return "\n".join(top) if top else "Couldn't fetch news."

def get_trending_searches():
    res = requests.get("https://trends.google.com/trends/trendingsearches/daily?geo=IN", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    searches = soup.select(".details-top span")
    return ", ".join(s.text.strip() for s in searches[:5]) if searches else "Couldn't fetch trending searches."

# ------------------ Tech & Programming ------------------
def get_programming_quote():
    res = requests.get("https://quotes.stormconsultancy.co.uk/random.json")
    if res.status_code == 200:
        data = res.json()
        return f"{data['quote']} — {data['author']}"
    return "Couldn't fetch programming quote."

def get_github_trending():
    res = requests.get("https://github.com/trending", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    repos = soup.select("h2 > a")
    if repos:
        repo = random.choice(repos)
        return f"Trending Repo: {repo.text.strip()} — https://github.com{repo['href']}"
    return "Couldn't fetch trending repo."

# ------------------ Example ------------------
if __name__ == "__main__":
    print(get_random_fact())
    print(get_word_of_the_day())
    print(get_quote_of_the_day())
    print(get_idiom())
    print(get_joke())
    print(get_riddle())
    print(get_cat_fact())
    print(get_did_you_know())
    print(get_today_in_history())
    print(get_top_news())
    print(get_trending_searches())
    print(get_programming_quote())
    print(get_github_trending())

