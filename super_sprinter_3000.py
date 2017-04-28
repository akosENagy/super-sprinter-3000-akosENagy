from flask import Flask
from flask import render_template
from jinja2 import Template


app = Flask(__name__)


@app.route('/')
@app.route('/list')
def render_list():
    return render_template('list.html')


@app.route('/story')
def render_form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
