from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

browser = None

def open_youtube_and_search(query):
    global browser

    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.get("https://www.youtube.com")
    time.sleep(3)
    search_box = browser.find_element(By.NAME, "search_query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    
    browser.execute_script("""
        const firstVideo = document.querySelector('#video-title');
        if (firstVideo) firstVideo.click();
    """)
    time.sleep(5)

    
    def ad_control_loop():
        is_muted = False
        while True:
            try:
                
                browser.execute_script("""
                    const skipBtn = document.querySelector('.ytp-ad-skip-button');
                    if (skipBtn) skipBtn.click();

                    const overlayAd = document.querySelector('.ytp-ad-overlay-close-button');
                    if (overlayAd) overlayAd.click();
                """)

                
                ad_playing = browser.execute_script("return document.querySelector('.ad-showing') !== null;")
                if ad_playing and not is_muted:
                    browser.execute_script("document.querySelector('video').muted = true;")
                    is_muted = True
                elif not ad_playing and is_muted:
                    browser.execute_script("document.querySelector('video').muted = false;")
                    is_muted = False

            except Exception as e:
                print("[Ad Control Error]:", e)
            time.sleep(2.5)

    threading.Thread(target=ad_control_loop, daemon=True).start()


def pause_video():
    global browser
    if browser:
        try:
            browser.find_element(By.TAG_NAME, "body").send_keys("k")  
        except Exception as e:
            print("[Pause Error]:", e)


def scroll_down():
    global browser
    if browser:
        try:
            browser.execute_script("window.scrollBy(0, 500);")
        except Exception as e:
            print("[Scroll Error]:", e)


def like_video():
    global browser
    if browser:
        try:
           
            like_button = browser.find_elements(By.XPATH, "//ytd-toggle-button-renderer")[0]
            like_button.click()
        except Exception as e:
            print("[Like Error]:", e)
