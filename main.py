
from ui_utils import set_log_widget, update_log
import tkinter as tk
from speech_engine import speak, listen
from commands import process_command
from PIL import Image, ImageTk, ImageSequence
import threading
import os

# Function to play animated GIF
class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        im = Image.open(path)
        seq = []
        try:
            while True:
                frame = im.copy().resize((128, 128), Image.Resampling.LANCZOS)
                seq.append(frame)
                im.seek(len(seq))  # next frame
        except EOFError:
            pass

        self.frames = [ImageTk.PhotoImage(img) for img in seq]
        self.delay = delay
        self.idx = 0
        self.cancel = False
        super().__init__(master, image=self.frames[0])
        self.after(self.delay, self.play)

    def play(self):
        if not self.cancel:
            self.config(image=self.frames[self.idx])
            self.idx = (self.idx + 1) % len(self.frames)
            self.after(self.delay, self.play)

    def stop(self):
        self.cancel = True

# Update log safely
def update_log(text):
    log.config(state=tk.NORMAL)
    log.insert(tk.END, text)
    log.see(tk.END)
    log.config(state=tk.DISABLED)

# AI Logic Thread
def run_ai():
    command = listen()
    if command:
        result = process_command(command)
        if result != "__async__":
            log.insert(tk.END, f"👤 You: {command}\n🤖 AI: {result}\n\n")
            log.see(tk.END)


def start_thread():
    t = threading.Thread(target=run_ai)
    t.daemon = True
    t.start()

# --- GUI SETUP ---

window = tk.Tk()
window.title("✨ AI Assistant")
window.geometry("600x600")
window.configure(bg="#1e1e2e")

# Title
title = tk.Label(window, text="🤖 Your AI Assistant", font=("Helvetica", 20, "bold"), fg="#f5c542", bg="#1e1e2e")
title.pack(pady=10)

# Avatar
if os.path.exists("avatar.gif"):
    try:
        avatar = AnimatedGIF(window, "avatar.gif", delay=100)
        avatar.pack(pady=10)
    except Exception as e:
        print(f"Error loading avatar.gif: {e}")
else:
    print("⚠️ avatar.gif not found!")

# Log Output Box
log = tk.Text(window, height=15, width=65, font=("Courier New", 10), bg="#2d2d44", fg="#ffffff", wrap="word")
set_log_widget(log)
log.pack(pady=10)
log.config(state=tk.DISABLED)

# Buttons
btn_frame = tk.Frame(window, bg="#1e1e2e")
btn_frame.pack()

listen_btn = tk.Button(btn_frame, text="🎤 Start Listening", font=("Arial", 12), bg="#45c4b0", fg="white", command=start_thread)
listen_btn.pack(side="left", padx=10)

exit_btn = tk.Button(btn_frame, text="❌ Exit", font=("Arial", 12), bg="#f55c47", fg="white", command=window.destroy)
exit_btn.pack(side="right", padx=10)

# Start voice greeting
try:
    speak("Hello! I'm ready to help.")
except Exception as e:
    print("Voice engine failed to speak:", e)

window.mainloop()
