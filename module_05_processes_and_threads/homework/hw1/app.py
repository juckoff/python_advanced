import subprocess
import shlex
import argparse


def flask_run(port):
    flask_run_command = shlex.split(f'python -m flask run -p {port}')
    subprocess.Popen(flask_run_command)

    pid = port_checker(port)
    process_killer(pid)


def port_checker(port):
    port_check_command = shlex.split(f'lsof -i :{port}')
    port_check_process = subprocess.run(port_check_command, stdout=subprocess.PIPE)
    output = port_check_process.stdout.decode('utf-8')
    if output:
        pid_of_running_flask_process = output.split('\n')[1].split(' ')[2]

        return pid_of_running_flask_process


def process_killer(pid):
    if pid:
        kill_command = shlex.split(f'kill -9 {pid}')
        subprocess.run(kill_command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='flask_app_start')
    parser.add_argument('--port', dest="port", required=True, type=int)
    args = parser.parse_args()
    flask_run(port=args.port)