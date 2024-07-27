import serial
import speech_recognition as sr

arduino_port = '/dev/cu.usbmodem1101'  # Replace with the correct port
baud_rate = 115200

arduino = serial.Serial(arduino_port, baud_rate)
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "turn on light" in command or "light on kar do" in command:
            arduino.write(b'turn on light\n')
        elif "turn off light" in command or "light off kar do" in command:
            arduino.write(b'turn off light\n')
        elif "lock the door" in command or "921" in command:
            arduino.write(b'rotate servo clockwise\n')
        elif "unlock the door" in command:
            arduino.write(b'rotate servo anticlockwise\n')

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
