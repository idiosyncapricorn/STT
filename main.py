import speech_recognition as sr

def main():
    # Initialize the recognizer
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("\nPlease say something...")

            # Capture the audio input
            audio = r.listen(source)

            try:
                # Convert speech to text using Google Speech Recognition
                output = r.recognize_google(audio)

                if output.lower() == "stop":
                    break
                print(f"You said: \n{output}\n")
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()