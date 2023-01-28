from module_05_processes_and_threads.homework.hw3.block_errors import ExceptionsHandler
import unittest


class TestExceptionsInput(unittest.TestCase):

    exceptions = (ZeroDivisionError, IndexError)

    def test_index_error(self):
        test_list = [1, 2, 3]
        with ExceptionsHandler(self.exceptions):
            test_index_error = test_list[3]

    def test_zero_division_error(self):
        with ExceptionsHandler(self.exceptions):
            test_zero_division_error = 1 / 0

    def test_exception_not_in_list(self):
        with self.assertRaises(NameError):
            with ExceptionsHandler(self.exceptions):
                test_name_error = test5
