import unittest
import os
#import keyboard
from keylogger import Keylogger

class TestCreatingFile(unittest.TestCase):
    def test_create_the_text_file_on_desktop(self):
        testKeylogger = Keylogger()
        testKeylogger.payloadFile('testfile_that_has_a_unique_name.txt')

        desktopPath = os.path.expanduser('~/Desktop')
        find = False
        for root, dirs, files in os.walk(desktopPath):
            if 'testfile_that_has_a_unique_name.txt' in files:
                find = True
        self.assertTrue(find)

    def test_text_file_has_cool_on_its_first_line(self):
        desktopPath = os.path.expanduser('~/Desktop')
        filePath = os.path.join(desktopPath, 'testfile_that_has_a_unique_name.txt')
        f = open(filePath, 'r')
        line = f.readline()
        f.close()
        self.assertEqual(line, 'cool\n')

        os.remove(filePath)


class TestKeylogger(unittest.TestCase):
    def test_key_press_is_recorded_into_keyLog(self):
        testKeylogger = Keylogger()
        emptyKeyLog = [0, 0, 0, 0]
        self.assertEqual(testKeylogger.keyLog, emptyKeyLog)

        #testKeylogger.keyboardEvent(keyboard.write('cool'))
        #newKeyLog = ['c', 'o', 'o', 'l']
        #self.assertEqual(testKeylogger.keyLog, newKeyLog)
