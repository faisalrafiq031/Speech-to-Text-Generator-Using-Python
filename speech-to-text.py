import speech_recognition
import time

def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        print("Listening... Speak into the microphone (say 'exit' to stop).")
        try:
            audio = microphone.listen(live_phone)
            phrase = microphone.recognize_google(audio, language='en')
            return phrase
        except speech_recognition.UnknownValueError:
            return "I couldn't understand that."
        except speech_recognition.RequestError as e:
            return f"Could not request results from Google Speech Recognition; {e}"

if __name__ == '__main__':
    print("Starting continuous listening mode...")
    with open('you_said_this.txt', 'a') as file:  # Open in append mode
        while True:
            phrase = record_voice()
            print(f"You said: {phrase}")
            
            # Append the recognized speech to the file
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
            file.write(f"{timestamp} {phrase}\n")

            # Exit condition
            if "exit" in phrase.lower():
                print("Exiting... Your speech has been saved.")
                break
