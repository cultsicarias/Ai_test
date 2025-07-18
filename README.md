# 🤖 AI Assistant

A sophisticated AI-powered desktop assistant with voice recognition, speech synthesis, and web automation capabilities. Built with Python and Tkinter, featuring an animated avatar and intuitive GUI.

## ✨ Features

### 🎤 Voice Interaction
- **Speech Recognition**: Listen to voice commands using advanced speech recognition
- **Text-to-Speech**: Natural voice responses with multiple TTS engines (pyttsx3, edge-tts)
- **Real-time Processing**: Instant command processing and response

### 🌐 Web Automation
- **YouTube Integration**: Search and play videos directly from voice commands
- **Web Search**: Google search functionality with voice commands
- **Website Navigation**: Open popular websites (GitHub, Reddit, etc.)

### 🖥️ System Control
- **Application Launch**: Open system applications (Notepad, etc.)
- **System Commands**: Shutdown computer, get system information
- **Time & Date**: Voice-activated time and date queries

### 🎨 Modern UI
- **Animated Avatar**: Customizable animated GIF avatar
- **Dark Theme**: Modern dark interface with Catppuccin-inspired colors
- **Real-time Logging**: Live command and response logging
- **Responsive Design**: Clean, intuitive user interface

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Windows 10/11 (for system commands)
- Microphone and speakers

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cultsicarias/Ai_Draft.git
   cd Ai_Draft
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 📋 Dependencies

- **pyttsx3**: Text-to-speech engine
- **SpeechRecognition**: Voice recognition
- **pyaudio**: Audio processing
- **tkinter**: GUI framework
- **pillow**: Image processing for avatar
- **edge-tts**: Microsoft Edge TTS engine
- **selenium**: Web automation
- **pygetwindow**: Window management
- **pyppeteer2**: Browser automation

## 🎯 Usage Examples

### Voice Commands

| Command | Action |
|---------|--------|
| "Play [video name] on YouTube" | Search and play YouTube videos |
| "What time is it?" | Get current time |
| "Open notepad" | Launch Notepad application |
| "Search for [query]" | Perform Google search |
| "Open GitHub" | Navigate to GitHub |
| "Good morning" | Get contextual greeting |
| "Help" | Show available commands |
| "Shut down the computer" | System shutdown |

### Example Interactions

```
👤 You: "Play Python tutorials on YouTube"
🤖 AI: "Searching and playing Python tutorials on YouTube."

👤 You: "What time is it?"
🤖 AI: "The current time is 14:30:25"

👤 You: "Search for machine learning"
🤖 AI: "Searching for machine learning"
```

## 🏗️ Project Structure

```
Ai_Draft/
├── main.py              # Main application entry point
├── commands.py          # Command processing logic
├── speech_engine.py     # Speech recognition and synthesis
├── ui_utils.py          # UI utilities and logging
├── web_control.py       # Web automation functions
├── requirements.txt     # Python dependencies
├── avatar.gif          # Animated avatar (optional)
├── main.spec           # PyInstaller specification
└── README.md           # This file
```

## 🔧 Customization

### Adding New Commands
Edit `commands.py` to add new voice commands:

```python
elif "your command" in command:
    # Your custom logic here
    response = "Your response"
    speak(response)
    return response
```

### Customizing the Avatar
Replace `avatar.gif` with your own animated GIF (128x128px recommended).

### Modifying the UI
Edit `main.py` to customize colors, layout, and styling.

## 🐛 Troubleshooting

### Common Issues

1. **Microphone not working**:
   - Check microphone permissions
   - Ensure pyaudio is properly installed

2. **Speech recognition issues**:
   - Speak clearly and in a quiet environment
   - Check internet connection (for Google Speech API)

3. **TTS not working**:
   - Verify pyttsx3 installation
   - Check system audio settings

### Build Issues
For PyInstaller builds, ensure all dependencies are included in `main.spec`.

## 📝 Development

### Building Executable
```bash
pyinstaller main.spec
```

### Testing
- Test voice commands in different environments
- Verify web automation functionality
- Check system integration features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational and personal use. Feel free to modify and distribute for non-commercial purposes.

## 🙏 Acknowledgments

- Speech recognition powered by Google Speech API
- TTS engines: pyttsx3 and Microsoft Edge TTS
- Web automation with Selenium and Pyppeteer
- UI inspired by modern design principles

---

**Made with ❤️ for AI enthusiasts and automation lovers**

## Notes
- Large build and dist files are excluded from the repository.
- For automation with browsers, ensure the appropriate driver (e.g., OperaDriver) is available in the `operadriver_win64` directory.
