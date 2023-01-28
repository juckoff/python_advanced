"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

import sys


class ChangeOutput:

    def __init__(self, io_object):
        self.io_object = io_object
        self.stdout_old_value = sys.stdout
        self.stderr_old_value = sys.stderr

    def __enter__(self):
        sys.stdout = self.io_object
        sys.stderr = self.io_object
        return sys.stdout, sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout_old_value
        sys.stderr = self.stderr_old_value
        return True
