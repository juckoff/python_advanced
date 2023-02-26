from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route("/all-links")

def all_links():
    links = ['/index', '/dogs', '/cats', '/cats/<int:cat_id>']
    for rule in app.url_map.iter_rules():
        if len(rule.defaults) >= len(rule.arguments):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template("all_links.html", links=links)


@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


if __name__ == '__main__':
    app.run(debug=True)
