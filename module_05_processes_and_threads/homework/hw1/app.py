import os
import shlex
import signal
import subprocess as sp
from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> list[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    command: str = f'lsof -i :{port}'

    args: list[str] = shlex.split(command)
    try:
        output: str = sp.check_output(args).decode()
    except sp.CalledProcessError:
        return []
    lines: list[str] = output.splitlines()[1:]
    pids: list[int] = [int(line.split()[1]) for line in lines]
    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: list[int] = get_pids(port)
    for pid in pids:
        os.kill(pid, signal.SIGKILL)


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
