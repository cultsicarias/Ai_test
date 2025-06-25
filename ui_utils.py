import tkinter as tk

log_widget = None

def set_log_widget(widget):
    global log_widget
    log_widget = widget

def update_log(text):
    if log_widget:
        log_widget.config(state=tk.NORMAL)
        log_widget.insert(tk.END, text + "\n")
        log_widget.see(tk.END)
        log_widget.config(state=tk.DISABLED)
