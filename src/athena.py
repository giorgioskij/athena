import sys
import signal
import os
import speech_recognition as sr
import beepy

from . import config as cfg
from . import daemonise

pidfile_path = cfg.paths['TEMP'] + 'athena.pid'
model_path = cfg.paths['MODEL']

class Athena(daemonise.daemon):

    def __init__(self):
        super().__init__(pidfile_path)
        self.interrupted = False
        self.model = model_path

    def run(self):
        from . import snowboydecoder

        detector = snowboydecoder.HotwordDetector(self.model, sensitivity=0.45)
        print('Listening... Press Ctrl+C to exit')

        # main loop
        detector.start(detected_callback=self.detectedCallback,
                    audio_recorder_callback=self.audioRecorderCallback,
                    interrupt_check=self.interrupt_callback,
                    sleep_time=0.01)

        detector.terminate()
        


    def audioRecorderCallback(self, fname):

        print("converting audio to text")
        
        r = sr.Recognizer()
        with sr.AudioFile(fname) as source:
            audio = r.record(source)  # read the entire audio file
        
        # recognize speech using Google Speech Recognition
        try:
            googletext = r.recognize_google(audio)

            print('google says %s' % googletext)

            self.interpret(googletext)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            beepy.beep("error")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            beepy.beep("error")

        os.remove(fname)
        return

    def interpret(self, text):
        if "lock" in text:
            os.system("loginctl lock-session")
        if "play" in text or "resume" in text:
            os.system("playerctl play")
        if "pause" in text or "stop" in text:
            os.system("playerctl pause")

        if ("shut" in text and "down" in text) or ("good" in text and "night" in text) or ("power" in text and "off" in text):
            os.system("systemctl poweroff")

        if "where" in text or "ring" in text or "phone" in text:
            os.system("kdeconnect-cli -d ddd47023b42c0c6a --ring")
        if "how" in text and "you" in text:
            beepy.beep(sound='ready')    


    def detectedCallback(self):
        print('recording audio...', end='', flush=True)
        beepy.beep(sound='coin')


    def signal_handler(self, signal, frame):
        self.interrupted = True


    def interrupt_callback(self):
        return self.interrupted   



def main():

    if len(sys.argv) == 1:
        print("What to do with athena?\nUsage: python athena.py (start/stop)")
        exit(1)

    command = sys.argv[1].lower()

    athena = Athena()

    if command == 'start':
        athena.start()
    elif command == 'stop':
        athena.stop()
