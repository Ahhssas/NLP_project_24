from flask import Flask, render_template, request, redirect, url_for

from search import search_func
from search import check


app = Flask(__name__)


# главная страница
@app.route('/')
def index():
    return render_template("index.html")


# статистика
@app.route('/rating')
def rating():
    return render_template("rating.html")


# поиск по корпусу
@app.route('/search')
def search():
    return render_template("search.html")


# результаты поиска
@app.route('/results')
def results():
    if not request.args:
        return redirect(url_for('index'))
    # получение запроса
    line_input = request.args.get('Enter')
    # обработка запроса
    query_results = search_func(request.args.get('Enter'))
    check_res = check(request.args.get('Enter'))
    return render_template("results.html", input_line=line_input, results=query_results, check=check_res)


if __name__ == '__main__':
    app.run(debug=True)
