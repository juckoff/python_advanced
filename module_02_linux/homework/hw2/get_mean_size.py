"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import os
import subprocess


def get_mean_size(ls_output_path: str) -> float:
    with open(ls_output_path, mode='r', encoding='utf-8') as text:
        size = 0
        count = 0
        for line in text:
            if len(line.split()) == 9 and line.split()[0].startswith("-rw") and line.split()[4].isdigit():
                size += float(line.split()[4])
                count += 1
        return size / count


if __name__ == "__main__":
    output = "output_mean_size_ls.txt"
    subprocess.call(f"ls -l ./ > {output}", shell=True)
    path = os.path.abspath("output_mean_size_ls.txt")
    average_file_size = get_mean_size(path)
    from ..hw1.get_summary_rss import size_fmt
    avg = size_fmt(average_file_size)
    print("Средний размер файла:", avg)
