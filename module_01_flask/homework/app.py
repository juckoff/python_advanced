import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/cars')
def test_function():
    return 'Это ноавя текстовая страничка, ответ сгенерирован в %s' % \
                      datetime.datetime.now().utcnow()
list_of_strings = ['Chevrolet', 'Renault', 'Ford', 'Lada']
my_str = ' '.join(list_of_strings)
print(my_str)


@app.route('/cats')
def test_function():
    def test_function():
        return 'Это ноавя текстовая страничка, ответ сгенерирован в %s' % \
               datetime.datetime.now().utcnow()
import random

print(random.choice(['корниш рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']))


@app.route('/get_time/now')
def test_function():
        return 'Это ноавя текстовая страничка, ответ сгенерирован в %s' % \
               datetime.datetime.now().utcnow()
import datetime

current_time = datetime.datetime.now().time()
print(f"Точное время {current_time}")


@app.route('/get_time/future')
def test_function():
    return 'Это ноавя текстовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


from datetime import datetime, timedelta

current_time_after_hour = (datetime.now() + timedelta(hours=1)).time()
print(f"Точное время через час будет {current_time_after_hour}")



@app.route('/get_random_word')
def test_function():
    return 'Это ноавя текстовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


import random

with open('Война_и_мир_Льва_Толстого.txt', 'r') as f:
    a = f.read()
print((random.choice(a.translate({ord(i): None for i in '.,!&:;«»„“'}).split())))



@app.route('/')
def main():
    """Say hello"""
    global index_counter
    print(index_counter)
    return "Hello World: %s" % str(index_counter)

@app.route('/counter')
def counter():
    global index_counter
    index_counter = 0
    while True:
      index_counter += 1

if __name__ == '__main__':
    app.run(threaded=True)