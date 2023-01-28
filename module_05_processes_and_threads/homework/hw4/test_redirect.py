from module_05_processes_and_threads.homework.hw4.redirect import ChangeOutput
import unittest
import sys


class TestChangeOutput(unittest.TestCase):

    def test_stdout(self):
        with open('test_input.txt', mode='r') as f:
            with ChangeOutput(f):
                self.assertTrue(sys.stdout == ChangeOutput(f).stdout_old_value)

    def test_stderr(self):
        with open('test_input.txt', mode='r') as f:
            with ChangeOutput(f):
                self.assertTrue(sys.stderr == ChangeOutput(f).stderr_old_value)
