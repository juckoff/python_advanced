"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os


def size_fmt(number, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(number) < 1024.0:
            return "%3.1f%s%s" % (number, unit, suffix)
        number /= 1024.0
    return "%.1f%s%s" % (number, "Yi", suffix)


def get_summary_rss(ps_output_file_path: str, file_name: str) -> str:
    for file in os.listdir(ps_output_file_path):
        if file == file_name:
            with open(file, mode='r', encoding='utf-8') as text:
                ram = 0
                for line in text:
                    if line.split()[5].isdigit():
                        ram += float(line.split()[5])
                return size_fmt(ram)


if __name__ == "__main__":
    path = "./"
    my_file = 'output_file.txt'
    print(get_summary_rss(path, my_file))
