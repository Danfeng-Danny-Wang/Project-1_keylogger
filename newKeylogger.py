from pynput.keyboard import Key, Listener
from playsound import playsound
import logging, os

#log_dir = os.path.expanduser('~/Desktop')
log_dir = ''
q = ["c", 'o', 'o', 'o']

logging.basicConfig(filename=(log_dir + 'Key_log.txt'),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)
    check(key)

def check(key):
    '''for chars in q:
        print(key(chars))
    nextChar=q[0]
    print("next and m: ", ord(nextChar), m.char())
    if(nextChar == m or nextChar.lower() == m):
        print("same")
        q.pop()
    else:
        reload()
    if(q == []):
        playsound('cool.wav')
        reload();
    '''
    if key==Key.enter:
        playsound('cool.wav')
    
def reload():
    q = ["c", 'o', 'o', 'o']

with Listener(on_press=on_press) as listener:
    listener.join()
