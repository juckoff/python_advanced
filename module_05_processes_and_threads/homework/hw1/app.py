import datetime
import os
import shlex
import signal
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


def run_with_port(user_port):
    try:
        app.run(debug=True, port=user_port)
    except OSError:
        command_str = f"lsof -Fp -i :{user_port}"
        command = shlex.split(command_str)
        result = subprocess.run(command, capture_output=True)
        processes = result.stdout.decode().split('\n')
        pids = set()

        for proc in processes:
            if proc.startswith('p'):
                pids.add(proc[1:])

        for PID in pids:
            os.kill(int(PID), signal.SIGKILL)
