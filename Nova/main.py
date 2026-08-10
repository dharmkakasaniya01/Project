from voice import NovaVoice
from commands import execute_command


def main():

    print("=" * 50)
    print("                 NOVA AI")
    print("=" * 50)

    print("\nStarting Nova...")

    voice = NovaVoice()

    print("\n✅ Nova is ready.")
    print("🎤 Listening for commands...")
    print("Press CTRL + C to stop Nova.")

    while True:

        command = voice.listen(
            timeout=None,
            phrase_time_limit=8
        )

        if not command:
            continue

        print(f"\n⚙️ Command: {command}")

        response = execute_command(command)

        if response:
            voice.speak(response)

        print("\n🎤 Listening again...")


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\n\n🛑 Nova stopped.")

    except Exception as e:
        print("\n❌ Nova error:")
        print(e)