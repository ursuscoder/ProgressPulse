from flask import Flask
from flask import jsonify, render_template

app = Flask(__name__)


@app.route('/')
def my_index_view():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
