import unittest
import os
from keylogger import Keylogger

class TestCreatingFile(unittest.TestCase):
    def test_create_the_text_file_on_desktop(self):
        testKeylogger = Keylogger()
        testKeylogger.payloadFile('test.txt')

        desktopPath = os.path.expanduser('~/Desktop')
        find = False
        for root, dirs, files in os.walk(desktopPath):
            if 'test.txt' in files:
                find = 1
        self.assertTrue(find)

    def test_text_file_has_cool_on_its_first_line(self):
        desktopPath = os.path.expanduser('~/Desktop')
        filePath = os.path.join(desktopPath, 'test.txt')
        f = open(filePath, 'r')
        line = f.readline()
        f.close()
        self.assertEqual(line, 'cool\n')

        os.remove(filePath)
