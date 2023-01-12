"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int) -> str:
    global storage
    storage[date] = number
    return f"Добавлено {date}: {number} рублей"


@app.route("/calculate/<int:year>")
def calculate_year(year: int) -> str:
    global storage
    storage[str(year)] = 0
    summa = [int(value) for key, value in storage.items() if key.startswith(
             str(year)) and len(key) == 8]
    storage[str(year)] = sum(summa)
    return f"Траты за {year} год: {storage[str(year)]} рублей"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int) -> str:
    year_month = "{}{}".format(year, month) if month > 9 else "{}0{}".format(year, month)
    storage[year_month] = 0
    summa = [int(value) for key, value in storage.items() if key.startswith(year_month)]
    storage[year_month] = sum(summa)
    return f"Траты за {year} год {month} месяц: {storage[year_month]} рублей"


if __name__ == "__main__":
    app.run(debug=True)