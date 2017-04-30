from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def render_list():
    return render_template('list.html')


@app.route('/story')
def render_form():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def save_post_data():

    form = request.form
    form_data_list = ["{}:{}".format(key, form[key]) for key in form]

    with open('stories.csv', 'w+') as file:
        file.write(','.join(form_data_list))

    return render_template('form.html')


if __name__ == '__main__':
    app.run()
