from flask import Flask
from flask import request
from flask import render_template
from mysql import Mysql

app = Flask(__name__)

@app.route('/index')
# def hello_world():
#     print('hello world!')
#     return 'hello world'
def name():
    page = request.args.get('page')
    if not page or int(page) == 0:
        page = 1
    db = Mysql()
    keyword = request.args.get('keyword')
    items = db.getItems(page, keyword)
    page_range = range(int(page) - 3, int(page) + 2)
    if int(page) < 4:
        page_range = range(1, int(page) + 4)
    return render_template('index.html', items=items, page=int(page), prange = page_range)

if __name__ == '__main__':
    # app.run(app.run(port=5000,host='127.0.0.1',debug=True))
    app.run()