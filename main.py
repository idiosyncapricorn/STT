  import speech_recognition as sr

  elif user_input == '2':
                def main():
                    #initialize the recognaizer
                    r = sr.Recognizer()
                    while True:
                        with sr.Microphone() as source:
                            r.adjust_for_ambient_noise(source)

                            print("\nplease say something....")

                            audio = r.listen(source)
                            output = r.recognize_google(audio)

                            try:
                                if output == "stop":
                                    break
                                print(f"You said... \n{output}\n")
                            except Exception as e:
                                print(f"Error {str(e)}")

                if __name__ == "__main__":
                    main()
