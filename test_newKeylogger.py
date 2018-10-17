import unittest, os
from pynput.keyboard import Key, Listener, Controller

from newKeylogger import KeyLogger

class TestKeyLogger(unittest.TestCase):
    def setUp(self):
        self.test = KeyLogger(fileName='\\testfile_that_has_a_unique_name.txt')
        self.keyboard = Controller()
        self.desktopPath = os.path.expanduser('~/Desktop')
        self.filePath = os.path.join(self.desktopPath,
                                'testfile_that_has_a_unique_name.txt')

    #def tearDown(self):
    #    self.keyboard = ''
    #    os.remove(self.filePath)

    def test_key_log_is_created(self):
        find = False
        for root, dirs, files in os.walk(self.desktopPath):
            if 'testfile_that_has_a_unique_name.txt' in files:
                find = True
        self.assertTrue(find)

    def test_key_press_is_created(self):
        self.test.run()
        self.keyboard.press('h')
        self.keyboard.press('i')

        keyLog = open(self.filePath, 'r')
        line1 = keyLog.readline()
        key1 = self.read_key_in_a_keylog_line(line1)
        line2 = keyLog.readline()
        key2 = self.read_key_in_a_keylog_line(line2)

        self.assertEqual(key1, 'h')
        self.assertEqual(key2, 'i')

    def read_key_in_a_keylog_line(self, line):
        line = line.strip().split()
        return line[2]

