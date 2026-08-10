# 🤖 NOVA — Natural Voice Operating Assistant

**NOVA** is a Python-based voice-controlled desktop assistant for Windows.

It allows you to control your computer using your voice — open and close applications, search Google or YouTube, open Windows tools, and perform other desktop actions without using the keyboard.

> 🎙️ **Speak → NOVA understands → NOVA performs the action**

---

## ✨ What Can NOVA Do?

NOVA currently supports commands for:

### 🌐 Web

* Open Google
* Open YouTube
* Search Google
* Search YouTube

Example:

```text
"Search Python tutorials"
"Search YouTube Valorant montage"
```

### 🖥️ Applications

NOVA can open supported applications such as:

* Google Chrome
* Microsoft Edge
* WhatsApp
* Discord
* Spotify
* Steam
* Photoshop
* Visual Studio Code
* VALORANT
* Armoury Crate
* Notepad
* Calculator

Example:

```text
"Open Chrome"
"Open VS Code"
"Open Spotify"
"Open Photoshop"
```

### ❌ Close Applications

You can also close supported applications using your voice.

```text
"Close Chrome"
"Close Spotify"
"Close VS Code"
```

### 🪟 Windows Controls

NOVA can open:

```text
"Open Settings"
"Open File Explorer"
"Open This PC"
"Open Calculator"
"Open Notepad"
```

### 🔊 Voice Response

NOVA doesn't just execute commands — it responds using text-to-speech.

Example:

```text
You: Open Chrome

NOVA: Opening Chrome, sir.
```

---

# 🚀 Getting Started

## 1. Requirements

Before running NOVA, make sure you have:

* Windows 10 or Windows 11
* Python 3.11+ recommended
* A working microphone
* Internet connection
* The applications you want NOVA to control

---

## 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/NOVA-Natural-Voice-Operating-Assistant.git
```

Then enter the project folder:

```bash
cd NOVA-Natural-Voice-Operating-Assistant
```

---

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

---

## 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 5. Start NOVA

Run:

```bash
python main.py
```

You should see:

```text
==============================================
                 NOVA AI
==============================================

Voice-controlled Windows assistant
Say 'Close Nova' to exit.

Preparing Nova microphone...
Please stay quiet for 2 seconds...

Microphone ready.

Nova: Nova is online. Command, sir!
```

NOVA is now ready for your voice commands. 🎤

---

# 🎙️ Commands

Here are some examples you can try:

| Say this                   | NOVA will               |
| -------------------------- | ----------------------- |
| `Open Chrome`              | Open Chrome             |
| `Open Edge`                | Open Microsoft Edge     |
| `Open YouTube`             | Open YouTube            |
| `Open Google`              | Open Google             |
| `Search Python`            | Search Google           |
| `Search YouTube Minecraft` | Search YouTube          |
| `Open WhatsApp`            | Open WhatsApp           |
| `Open Discord`             | Open Discord            |
| `Open Spotify`             | Open Spotify            |
| `Open Steam`               | Open Steam              |
| `Open Photoshop`           | Open Photoshop          |
| `Open VS Code`             | Open Visual Studio Code |
| `Open Valorant`            | Launch VALORANT         |
| `Open Calculator`          | Open Calculator         |
| `Open Notepad`             | Open Notepad            |
| `Open File Explorer`       | Open File Explorer      |
| `Open Settings`            | Open Windows Settings   |
| `Open This PC`             | Open This PC            |
| `Close Chrome`             | Close Chrome            |
| `Close Spotify`            | Close Spotify           |
| `Close VS Code`            | Close VS Code           |
| `Close Nova`               | Exit NOVA               |

---

# 🧠 Speech Recognition

NOVA uses speech recognition to understand voice commands.

It also includes command normalization to handle common speech-recognition mistakes.

For example:

```text
"what app"        → WhatsApp
"photo shop"      → Photoshop
"valorent"        → VALORANT
"visual studio"   → VS Code
"you tube"        → YouTube
"microsoft hedge" → Microsoft Edge
```

This makes NOVA easier to use with normal speech.

---

# 📂 Project Structure

```text
NOVA/
│
├── main.py
├── voice.py
├── commands.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Controls the main NOVA program and command loop.

### `voice.py`

Handles:

* Microphone input
* Speech recognition
* Text-to-speech
* Microphone calibration

### `commands.py`

Handles:

* Command normalization
* Application launching
* Application closing
* Google searches
* YouTube searches
* Windows tools

---

# ⚙️ How It Works

```text
       🎤 Your Voice
             │
             ▼
     Speech Recognition
             │
             ▼
     Command Normalization
             │
             ▼
      Command Processor
             │
       ┌─────┴─────┐
       ▼           ▼
   Windows       Internet
   Actions        Search
       │           │
       └─────┬─────┘
             ▼
        NOVA Response
             │
             ▼
           🔊 TTS
```

---

# 🛠️ Technologies

* **Python**
* **SpeechRecognition**
* **Google Speech Recognition**
* **pyttsx3**
* **PyAudio**
* **PowerShell**
* **Windows subprocess**
* **Webbrowser**

---

# ⚠️ Important

NOVA is currently designed for **Windows**.

Some commands depend on applications being installed on your computer.

For example, if Photoshop is not installed, saying:

```text
Open Photoshop
```

will not work.

Internet access is required for Google Speech Recognition and web searches.

---

# 🔮 Future Plans

NOVA is actively being developed.

Planned features include:

* 🎙️ `"Nova"` wake-word detection
* 😴 Sleep / wake mode
* 🔊 Volume control
* 🔒 Lock, sleep, restart and shutdown
* 📊 CPU and RAM monitoring
* 🔋 Battery information
* 📁 Voice-controlled file management
* 🧠 Personal memory
* 💬 More natural-language commands
* 🖥️ Modern NOVA GUI
* 📜 Command history
* 🤖 Advanced AI integration
* ⚡ Faster voice response

---

# 🤝 Contributing

Want to improve NOVA?

You can:

1. Fork the repository
2. Create a new branch
3. Add your feature or improvement
4. Test your changes
5. Create a Pull Request

Ideas and improvements are welcome!

---

# ⭐ Support

If you like NOVA, consider giving the repository a ⭐ on GitHub.

---

## 👨‍💻 Author

**Dharm Kakasaniya**

Built with Python, voice recognition, and a lot of experimentation. 🚀

---

### 🚀 NOVA

**Your voice. Your computer. Your commands.**
