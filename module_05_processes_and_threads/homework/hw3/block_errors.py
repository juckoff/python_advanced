"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""


class ExceptionsHandler:

    def __init__(self, exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            return True
        elif exc_type not in self.exceptions:
            raise exc_type
