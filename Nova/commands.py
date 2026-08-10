import os
import subprocess
import webbrowser
import ctypes

from pathlib import Path
from urllib.parse import quote_plus


# =========================================================
# USER HOME
# =========================================================

USER_HOME = Path.home()


# =========================================================
# COMMON FOLDERS
# =========================================================

FOLDERS = {

    "desktop":
        USER_HOME / "Desktop",

    "downloads":
        USER_HOME / "Downloads",

    "documents":
        USER_HOME / "Documents",

    "pictures":
        USER_HOME / "Pictures",

    "videos":
        USER_HOME / "Videos",

    "music":
        USER_HOME / "Music",
}


# =========================================================
# CUSTOM FOLDERS
# =========================================================
#
# અહીં તારા પોતાના folders add કરી શકીશ.
#
# Example:
#
# "nova":
#     Path(r"D:\Projects\Nova AI"),
#
# "college":
#     Path(r"D:\College"),
#
# =========================================================

CUSTOM_FOLDERS = {

    # "nova": Path(r"D:\Projects\Nova AI"),

    # "college": Path(r"D:\College"),

    # "projects": Path(r"D:\Projects"),

}


FOLDERS.update(CUSTOM_FOLDERS)


# =========================================================
# OPEN FOLDER
# =========================================================

def open_folder(path):

    try:

        path = Path(path)

        if path.exists():

            os.startfile(
                str(path)
            )

            return True

        return False

    except Exception as e:

        print("Folder error:", e)

        return False


# =========================================================
# THIS PC
# =========================================================

def open_this_pc():

    try:

        subprocess.Popen(
            [
                "explorer.exe",
                "shell:MyComputerFolder"
            ]
        )

        return True

    except Exception as e:

        print("This PC error:", e)

        return False


# =========================================================
# OPEN DRIVE
# =========================================================

def open_drive(letter):

    try:

        drive = f"{letter.upper()}:\\"

        if os.path.exists(drive):

            os.startfile(drive)

            return True

        return False

    except Exception as e:

        print("Drive error:", e)

        return False


# =========================================================
# APPLICATIONS
# =========================================================

APP_COMMANDS = {

    # -------------------------
    # Browsers
    # -------------------------

    "chrome":
        "chrome",

    "google chrome":
        "chrome",

    "edge":
        "msedge",

    "microsoft edge":
        "msedge",


    # -------------------------
    # Windows
    # -------------------------

    "notepad":
        "notepad.exe",

    "calculator":
        "calc.exe",

    "calc":
        "calc.exe",

    "paint":
        "mspaint.exe",

    "task manager":
        "taskmgr.exe",


    # -------------------------
    # Development
    # -------------------------

    "vs code":
        "code",

    "visual studio code":
        "code",


    # -------------------------
    # Apps
    # -------------------------

    "discord":
        "discord",

    "spotify":
        "spotify",

    "steam":
        "steam",

    "whatsapp":
        "whatsapp",


    # -------------------------
    # Adobe
    # -------------------------

    "photoshop":
        "photoshop",


    # -------------------------
    # ASUS
    # -------------------------

    "armoury crate":
        "armourycrate",


    # -------------------------
    # Explorer
    # -------------------------

    "file explorer":
        "explorer.exe",

    "explorer":
        "explorer.exe",
}


# =========================================================
# OPEN APP
# =========================================================

def open_app(command):

    for name, executable in APP_COMMANDS.items():

        if name in command:

            try:

                subprocess.Popen(
                    executable,
                    shell=True
                )

                return True

            except Exception as e:

                print(
                    f"Could not open {name}:",
                    e
                )

                return False

    return False


# =========================================================
# YOUTUBE
# =========================================================

def open_youtube():

    try:

        webbrowser.open(
            "https://www.youtube.com"
        )

        return True

    except Exception:

        return False


# =========================================================
# GOOGLE
# =========================================================

def open_google():

    try:

        webbrowser.open(
            "https://www.google.com"
        )

        return True

    except Exception:

        return False


# =========================================================
# GOOGLE SEARCH
# =========================================================

def google_search(command):

    phrases = [

        "search google for",
        "search google",
        "google search for",
        "google search",
        "search for",

    ]

    for phrase in phrases:

        if phrase in command:

            query = command.replace(
                phrase,
                "",
                1
            ).strip()

            if query:

                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(query)
                )

                webbrowser.open(url)

                return True

    return False


# =========================================================
# YOUTUBE SEARCH
# =========================================================

def youtube_search(command):

    phrases = [

        "search youtube for",
        "search youtube",
        "youtube search for",
        "youtube search",

    ]

    for phrase in phrases:

        if phrase in command:

            query = command.replace(
                phrase,
                "",
                1
            ).strip()

            if query:

                url = (
                    "https://www.youtube.com/results"
                    "?search_query="
                    + quote_plus(query)
                )

                webbrowser.open(url)

                return True

    return False


# =========================================================
# CLOSE PROCESS
# =========================================================

def close_process(process_name):

    try:

        result = subprocess.run(

            [
                "taskkill",
                "/F",
                "/IM",
                process_name
            ],

            capture_output=True,
            text=True
        )

        return result.returncode == 0

    except Exception as e:

        print("Close error:", e)

        return False


# =========================================================
# CLOSE APPLICATION
# =========================================================

CLOSE_COMMANDS = {

    "chrome": [
        "chrome.exe"
    ],

    "google chrome": [
        "chrome.exe"
    ],

    "edge": [
        "msedge.exe"
    ],

    "microsoft edge": [
        "msedge.exe"
    ],

    "discord": [
        "Discord.exe"
    ],

    "spotify": [
        "Spotify.exe"
    ],

    "whatsapp": [
        "WhatsApp.exe"
    ],

    "photoshop": [
        "Photoshop.exe"
    ],

    "steam": [
        "steam.exe"
    ],

    "valorant": [
        "VALORANT-Win64-Shipping.exe"
    ],

    "notepad": [
        "notepad.exe"
    ],

    "vs code": [
        "Code.exe"
    ],

    "visual studio code": [
        "Code.exe"
    ],

    "armoury crate": [
        "ArmouryCrate.exe",
        "ArmouryCrate.UserSessionHelper.exe"
    ],
}


def close_app(command):

    # -----------------------------------------------------
    # YOUTUBE
    # -----------------------------------------------------

    if (
        "close youtube" in command
        or "exit youtube" in command
        or "quit youtube" in command
        or "stop youtube" in command
    ):

        chrome = close_process(
            "chrome.exe"
        )

        edge = close_process(
            "msedge.exe"
        )

        return chrome or edge


    # -----------------------------------------------------
    # GOOGLE
    # -----------------------------------------------------

    if (
        "close google" in command
        or "exit google" in command
        or "quit google" in command
        or "close google search" in command
    ):

        chrome = close_process(
            "chrome.exe"
        )

        edge = close_process(
            "msedge.exe"
        )

        return chrome or edge


    # -----------------------------------------------------
    # OTHER APPS
    # -----------------------------------------------------

    for name, processes in CLOSE_COMMANDS.items():

        if name in command:

            for process in processes:

                if close_process(process):

                    return True

            return False

    return False


# =========================================================
# SYSTEM COMMANDS
# =========================================================

def system_command(command):

    # -------------------------
    # Lock PC
    # -------------------------

    if (
        "lock pc" in command
        or "lock computer" in command
        or "lock my pc" in command
    ):

        ctypes.windll.user32.LockWorkStation()

        return "PC locked."


    # -------------------------
    # Settings
    # -------------------------

    if "open settings" in command:

        subprocess.Popen(
            "start ms-settings:",
            shell=True
        )

        return "Opening settings."


    # -------------------------
    # Task Manager
    # -------------------------

    if "open task manager" in command:

        subprocess.Popen(
            "taskmgr.exe"
        )

        return "Opening Task Manager."


    return None


# =========================================================
# MAIN COMMAND PROCESSOR
# =========================================================

def execute_command(command):

    command = command.lower().strip()


    if not command:

        return "I didn't hear a command."


    # =====================================================
    # CLOSE COMMANDS
    # =====================================================

    if (
        command.startswith("close ")
        or command.startswith("exit ")
        or command.startswith("quit ")
        or command.startswith("stop ")
    ):

        if close_app(command):

            return "Closed."

        return "I couldn't close it."


    # =====================================================
    # THIS PC
    # =====================================================

    if (
        "this pc" in command
        or "my computer" in command
        or "open computer" in command
        or command == "computer"
    ):

        if open_this_pc():

            return "Opening This PC."

        return "I couldn't open This PC."


    # =====================================================
    # DRIVES
    # =====================================================

    drive_words = {

        "c drive": "C",
        "c disk": "C",
        "drive c": "C",

        "d drive": "D",
        "d disk": "D",
        "drive d": "D",

        "e drive": "E",
        "e disk": "E",
        "drive e": "E",

        "f drive": "F",
        "f disk": "F",
        "drive f": "F",

        "g drive": "G",
        "g disk": "G",
        "drive g": "G",

    }


    for word, letter in drive_words.items():

        if word in command:

            if open_drive(letter):

                return (
                    f"Opening {letter} drive."
                )

            return (
                f"{letter} drive is not available."
            )


    # =====================================================
    # DIRECT FOLDERS
    # =====================================================

    for folder_name, folder_path in FOLDERS.items():

        if folder_name in command:

            if open_folder(folder_path):

                return (
                    f"Opening {folder_name}."
                )

            return (
                f"I couldn't find your "
                f"{folder_name} folder."
            )


    # =====================================================
    # YOUTUBE SEARCH
    # =====================================================

    if youtube_search(command):

        return "Searching YouTube."


    # =====================================================
    # GOOGLE SEARCH
    # =====================================================

    if google_search(command):

        return "Searching Google."


    # =====================================================
    # OPEN YOUTUBE
    # =====================================================

    if (
        "open youtube" in command
        or "launch youtube" in command
        or "start youtube" in command
    ):

        if open_youtube():

            return "Opening YouTube."

        return "I couldn't open YouTube."


    # =====================================================
    # OPEN GOOGLE
    # =====================================================

    if (
        "open google" in command
        or "launch google" in command
        or "start google" in command
    ):

        if open_google():

            return "Opening Google."

        return "I couldn't open Google."


    # =====================================================
    # OPEN APPLICATION
    # =====================================================

    if open_app(command):

        return "Opening it."


    # =====================================================
    # SYSTEM
    # =====================================================

    response = system_command(command)

    if response:

        return response


    # =====================================================
    # NOVA BASIC COMMANDS
    # =====================================================

    if "who are you" in command:

        return (
            "I am Nova, your personal "
            "AI assistant."
        )


    if "what is your name" in command:

        return "My name is Nova."


    # =====================================================
    # UNKNOWN
    # =====================================================

    return (
        "Sorry, I don't know that command yet."
    )