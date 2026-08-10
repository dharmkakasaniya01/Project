import speech_recognition as sr
import pyttsx3
import time


class NovaVoice:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # -----------------------------
        # Speech recognition settings
        # -----------------------------

        self.recognizer.energy_threshold = 280
        self.recognizer.dynamic_energy_threshold = True

        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5

        self.recognizer.pause_threshold = 0.6
        self.recognizer.phrase_threshold = 0.2
        self.recognizer.non_speaking_duration = 0.3

        # -----------------------------
        # Text to speech
        # -----------------------------

        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            185
        )

        self.engine.setProperty(
            "volume",
            1.0
        )

        voices = self.engine.getProperty("voices")

        if voices:

            # Default available voice
            self.engine.setProperty(
                "voice",
                voices[0].id
            )

        # -----------------------------
        # Microphone calibration
        # -----------------------------

        self.calibrate_microphone()


    def calibrate_microphone(self):

        print("🎤 Calibrating microphone...")

        try:

            with sr.Microphone() as source:

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

            # Prevent threshold becoming too high

            if self.recognizer.energy_threshold > 700:

                self.recognizer.energy_threshold = 400

            print("✅ Microphone ready.")

        except Exception as e:

            print("❌ Microphone error:")
            print(e)


    def speak(self, text):

        print(f"Nova: {text}")

        self.engine.say(text)

        self.engine.runAndWait()

        # Small delay to prevent immediate microphone pickup
        time.sleep(0.2)


    def listen(
        self,
        timeout=None,
        phrase_time_limit=8
    ):

        try:

            with sr.Microphone() as source:

                print("🎤 Listening...")

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            text = text.lower().strip()

            print(f"You: {text}")

            return text


        except sr.WaitTimeoutError:

            return ""


        except sr.UnknownValueError:

            print("❓ Could not understand.")

            return ""


        except sr.RequestError:

            print(
                "❌ Speech recognition service "
                "is unavailable."
            )

            return ""


        except Exception as e:

            print("❌ Voice error:")
            print(e)

            return ""