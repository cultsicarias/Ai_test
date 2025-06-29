import os
import threading
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

from speech_engine import speak, listen
from commands import process_command
from ui_utils import set_log_widget

# --- ANIMATED GIF CLASS ---
class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        im = Image.open(path)
        seq = []
        try:
            while True:
                frame = im.copy().resize((128, 128), Image.Resampling.LANCZOS)
                seq.append(frame)
                im.seek(len(seq))
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

# --- LOG HANDLER ---
def update_log(text):
    log.config(state=tk.NORMAL)
    log.insert(tk.END, text)
    log.see(tk.END)
    log.config(state=tk.DISABLED)

# --- VOICE COMMAND THREAD ---
def run_ai():
    command = listen()
    if command:
        result = process_command(command)
        if result != "__async__":
            update_log(f"👤 You (Voice): {command}\n🤖 AI: {result}\n\n")

# --- TEXT COMMAND HANDLER ---
def run_text_command():
    command = input_entry.get().strip()
    if command:
        input_entry.delete(0, tk.END)
        update_log(f"👤 You (Typed): {command}\n")
        threading.Thread(target=process_and_log, args=(command,), daemon=True).start()

def process_and_log(command):
    result = process_command(command)
    if result != "__async__":
        update_log(f"🤖 AI: {result}\n\n")

# --- MAIN GUI ---
window = tk.Tk()
window.title("✨ AI Assistant")
window.geometry("600x650")
window.configure(bg="#1e1e2e")

title = tk.Label(window, text="🤖 Your AI Assistant", font=("Helvetica", 20, "bold"), fg="#f5c542", bg="#1e1e2e")
title.pack(pady=10)

if os.path.exists("avatar.gif"):
    try:
        avatar = AnimatedGIF(window, "avatar.gif", delay=100)
        avatar.pack(pady=10)
    except Exception as e:
        print(f"Error loading avatar.gif: {e}")
else:
    print("⚠️ avatar.gif not found!")

log = tk.Text(window, height=15, width=65, font=("Courier New", 10), bg="#2d2d44", fg="#ffffff", wrap="word")
log.pack(pady=10)
log.config(state=tk.DISABLED)
set_log_widget(log)

# --- Text Command Input ---
input_entry = tk.Entry(window, font=("Courier New", 12), width=55, bg="#3b3b58", fg="#ffffff")
input_entry.pack(pady=10)
input_entry.bind("<Return>", lambda event: run_text_command())  # Press Enter to send

# --- Buttons ---
btn_frame = tk.Frame(window, bg="#1e1e2e")
btn_frame.pack()

listen_btn = tk.Button(btn_frame, text="🎤 Start Listening", font=("Arial", 12), bg="#45c4b0", fg="white", command=lambda: threading.Thread(target=run_ai, daemon=True).start())
listen_btn.pack(side="left", padx=10)

send_btn = tk.Button(btn_frame, text="📨 Send", font=("Arial", 12), bg="#557ef8", fg="white", command=run_text_command)
send_btn.pack(side="left", padx=10)

exit_btn = tk.Button(btn_frame, text="❌ Exit", font=("Arial", 12), bg="#f55c47", fg="white", command=window.destroy)
exit_btn.pack(side="right", padx=10)

# --- Greeting ---
try:
    speak("Hello! I'm ready to help.")
except Exception as e:
    print("Voice engine failed to speak:", e)

window.mainloop()
