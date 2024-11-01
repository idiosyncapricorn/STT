import speech_recognition as sr
from libc.stdio cimport printf

# Declare types to improve performance
cdef class SpeechRecognizer:
    def recognize_speech(self, sr.Recognizer recognizer, sr.AudioSource source) -> str:
        """
        Capture and recognize speech from the given audio source.
        Returns the recognized text or raises an error if speech is unclear.
        """
        try:
            # Adjust for ambient noise and capture audio
            recognizer.adjust_for_ambient_noise(source)
            printf("\nListening... Please say something.\n")
            audio = recognizer.listen(source)

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            printf("Sorry, I couldn't understand what you said. Please try again.\n")
        except sr.RequestError as e:
            printf("Could not request results from Google Speech Recognition service; %s\n", str(e))
        except Exception as e:
            printf("An unexpected error occurred: %s\n", str(e))

    def main(self):
        cdef sr.Recognizer recognizer = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                # Get recognized text from the audio input
                output = self.recognize_speech(recognizer, source)

                if output:
                    # If "stop" is spoken, exit the loop
                    if output.lower() == "stop":
                        printf("Stopping speech recognition.\n")
                        break
                    printf("You said: \n%s\n\n", output)

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.main()