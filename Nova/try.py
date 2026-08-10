import webbrowser
import subprocess

def open_windows_app(app_name):
    try:
        powershell_command = f"""
        $app = Get-StartApps |
        Where-Object {{ $_.Name -like '*{app_name}*' }} |
        Select-Object -First 1

        if ($app) {{
            Write-Output $app.AppID
        }}
        """

        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", powershell_command],
            capture_output=True,
            text=True,
            timeout=5
        )

        app_id = result.stdout.strip()

        if app_id:
            subprocess.Popen([
                "explorer.exe",
                f"shell:AppsFolder\\{app_id}"
            ])
            return True

        return False

    except Exception as error:
        print("Open app error:", error)
        return False


def close_app(app_name):
    processes = {
        "chrome": ["chrome.exe"],
        "google chrome": ["chrome.exe"],
        "edge": ["msedge.exe"],
        "microsoft edge": ["msedge.exe"],
        "whatsapp": ["WhatsApp.exe", "WhatsApp.Root.exe", "WhatsAppHost.exe"],
        "discord": ["Discord.exe", "DiscordPTB.exe", "DiscordCanary.exe"],
        "spotify": ["Spotify.exe"],
        "steam": ["steam.exe", "steamwebhelper.exe"],
        "photoshop": ["Photoshop.exe"],
        "vs code": ["Code.exe"],
        "vscode": ["Code.exe"],
        "visual studio code": ["Code.exe"],
        "valorant": ["VALORANT-Win64-Shipping.exe"],
        "armoury crate": [
            "ArmouryCrate.exe",
            "ArmouryCrate.UserSessionHelper.exe",
            "ArmouryCrateControlInterface.exe"
        ],
        "armory crate": [
            "ArmouryCrate.exe",
            "ArmouryCrate.UserSessionHelper.exe",
            "ArmouryCrateControlInterface.exe"
        ],
        "settings": ["SystemSettings.exe"],
        "notepad": ["notepad.exe"],
        "calculator": ["CalculatorApp.exe", "Calculator.exe"]
    }

    process_list = processes.get(app_name)

    if not process_list:
        return False

    closed = False

    for process in process_list:
        try:
            result = subprocess.run(
                ["taskkill", "/F", "/IM", process, "/T"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                closed = True

        except Exception as error:
            print("Close error:", process, error)

    return closed


def normalize_command(command):
    command = command.lower().strip()

    armoury_variations = [
        "armoury crate",
        "armory crate",
        "armoury create",
        "armory create",
        "armor crate",
        "armor create",
        "armour create",
        "armoury great",
        "armory great",
        "armoury cr8",
        "armory cr8",
        "armoury create it",
        "armory created",
        "armoury created"
    ]

    for variation in armoury_variations:
        if variation in command:
            command = command.replace(variation, "armoury crate")

    edge_variations = [
        "microsoft edge",
        "microsoft hedge",
        "microsoft ledge",
        "microsoft etch",
        "microsoft age",
        "microsoft h",
        "microsoft eggs",
        "microsoft egg",
        "ms edge",
        "msedge",
        "open edge",
        "open microsoft edge"
    ]

    for variation in edge_variations:
        if variation in command:
            command = command.replace(variation, "edge")

    if command in ["hedge", "ledge", "etch", "age", "eggs", "egg"]:
        command = "edge"

    whatsapp_variations = [
        "what's app",
        "what app",
        "whats app",
        "whatsapp",
        "what's up",
        "whats up"
    ]

    for variation in whatsapp_variations:
        if variation in command:
            command = command.replace(variation, "whatsapp")

    discord_variations = [
        "discord",
        "this cord",
        "dis cord",
        "disc cord"
    ]

    for variation in discord_variations:
        if variation in command:
            command = command.replace(variation, "discord")

    photoshop_variations = [
        "photoshop",
        "photo shop",
        "photos hop",
        "photo shot"
    ]

    for variation in photoshop_variations:
        if variation in command:
            command = command.replace(variation, "photoshop")

    valorant_variations = [
        "valorant",
        "valorent",
        "valor aunt",
        "valor ant",
        "valor and"
    ]

    for variation in valorant_variations:
        if variation in command:
            command = command.replace(variation, "valorant")

    vscode_variations = [
        "vs code",
        "vs coding",
        "vs coded",
        "visual studio code",
        "visual studio"
    ]

    for variation in vscode_variations:
        if variation in command:
            command = command.replace(variation, "vs code")

    spotify_variations = [
        "spotify",
        "spotty five",
        "spot if i"
    ]

    for variation in spotify_variations:
        if variation in command:
            command = command.replace(variation, "spotify")

    steam_variations = [
        "steam",
        "st eam"
    ]

    for variation in steam_variations:
        if variation in command:
            command = command.replace(variation, "steam")

    settings_variations = [
        "settings",
        "setting",
        "windows settings",
        "window settings"
    ]

    for variation in settings_variations:
        if variation in command:
            command = command.replace(variation, "settings")

    youtube_variations = [
        "youtube",
        "you tube",
        "you too"
    ]

    for variation in youtube_variations:
        if variation in command:
            command = command.replace(variation, "youtube")

    return command.strip()


def execute_command(command):
    command = normalize_command(command)

    print("Normalized command:", command)

    if command.startswith("close "):
        app_name = command.replace("close ", "", 1).strip()

        if close_app(app_name):
            return "Closing " + app_name + ", sir."
        else:
            return "I couldn't find " + app_name + " running."

    if command.startswith("search youtube"):
        query = command.replace("search youtube", "", 1).strip()

        if query:
            url = (
                "https://www.youtube.com/results?search_query="
                + query.replace(" ", "+")
            )
            webbrowser.open(url)
            return "Searching YouTube for " + query + ", sir."

        return "What should I search on YouTube, sir?"

    if command.startswith("search "):
        query = command.replace("search ", "", 1).strip()

        if query:
            url = (
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )
            webbrowser.open(url)
            return "Searching for " + query + ", sir."

        return "What should I search for, sir?"

    if command == "youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube, sir."

    if command == "google":
        webbrowser.open("https://www.google.com")
        return "Opening Google, sir."

    if command in ["chrome", "google chrome"]:
        try:
            subprocess.Popen(["cmd", "/c", "start", "", "chrome"])
            return "Opening Chrome, sir."
        except:
            return "I couldn't open Chrome."

    if command == "edge":
        try:
            subprocess.Popen(["cmd", "/c", "start", "", "msedge"])
            return "Opening Microsoft Edge, sir."
        except:
            return "I couldn't open Edge."

    if command == "settings":
        try:
            subprocess.Popen(["cmd", "/c", "start", "", "ms-settings:"])
            return "Opening Settings, sir."
        except:
            return "I couldn't open Settings."

    if command in ["this pc", "my pc", "computer"]:
        try:
            subprocess.Popen([
                "explorer.exe",
                "shell:MyComputerFolder"
            ])
            return "Opening This PC, sir."
        except:
            return "I couldn't open This PC."

    if command in ["file explorer", "explorer"]:
        try:
            subprocess.Popen(["explorer.exe"])
            return "Opening File Explorer, sir."
        except:
            return "I couldn't open File Explorer."

    if command in ["calculator", "calc"]:
        try:
            subprocess.Popen(["calc.exe"])
            return "Opening Calculator, sir."
        except:
            return "I couldn't open Calculator."

    if command == "notepad":
        try:
            subprocess.Popen(["notepad.exe"])
            return "Opening Notepad, sir."
        except:
            return "I couldn't open Notepad."

    if command == "whatsapp":
        if open_windows_app("WhatsApp"):
            return "Opening WhatsApp, sir."
        return "I couldn't find WhatsApp."

    if command == "discord":
        if open_windows_app("Discord"):
            return "Opening Discord, sir."
        return "I couldn't find Discord."

    if command == "photoshop":
        if open_windows_app("Photoshop"):
            return "Opening Photoshop, sir."
        return "I couldn't find Photoshop."

    if command == "armoury crate":
        if open_windows_app("Armoury Crate"):
            return "Opening Armoury Crate, sir."
        return "I couldn't find Armoury Crate."

    if command == "spotify":
        if open_windows_app("Spotify"):
            return "Opening Spotify, sir."
        return "I couldn't find Spotify."

    if command == "steam":
        if open_windows_app("Steam"):
            return "Opening Steam, sir."
        return "I couldn't find Steam."

    if command == "valorant":
        if open_windows_app("VALORANT"):
            return "Launching Valorant, sir."
        return "I couldn't find Valorant."

    if command == "vs code":
        if open_windows_app("Visual Studio Code"):
            return "Opening Visual Studio Code, sir."
        return "I couldn't find Visual Studio Code."

    return "I don't know that command yet, sir."