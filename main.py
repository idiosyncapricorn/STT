import speech_recognition as sr

def recognize_speech(recognizer, source):
    """
    Capture and recognize speech from the given audio source.
    Returns the recognized text or raises an error if speech is unclear.
    """
    try:
        # Adjust for ambient noise and capture audio
        recognizer.adjust_for_ambient_noise(source)
        print("\nListening... Please say something.")
        audio = recognizer.listen(source)

        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            # Get recognized text from the audio input
            output = recognize_speech(recognizer, source)

            if output:
                # If "stop" is spoken, exit the loop
                if output.lower() == "stop":
                    print("Stopping speech recognition.")
                    break
                print(f"You said: \n{output}\n")

if __name__ == "__main__":
    main()