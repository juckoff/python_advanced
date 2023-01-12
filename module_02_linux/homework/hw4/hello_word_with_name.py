"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<name>")
def hello_world(name: str) -> str:
    day_rus = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']
    day = datetime.datetime.today().weekday()
    if day in [0, 1, 3, 6]:
        return f"Привет, {name}. Хорошего {day_rus[day]}!"
    return f"Привет, {name}. Хорошей {day_rus[day]}!"


if __name__ == "__main__":
    app.run(debug=True)