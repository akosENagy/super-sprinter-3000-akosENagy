from flask import Flask, render_template, request
import data_manager

app = Flask(__name__, static_url_path="/static")


@app.route('/')
@app.route('/list')
def render_list():
    user_stories = data_manager.get_data_from_file('stories.csv')

    return render_template('list.html', user_stories=user_stories)


@app.route('/story')
def render_form():
    return render_template('form.html', title="Add New Story")


@app.route('/story', methods=['POST'])
def save_post_data():

    form_data_list = ["{}:{}".format(key, request.form[key]) for key in request.form]
    data_manager.write_to_file(form_data_list)

    return render_template('form.html', title="Add New Story")


@app.route('/story/<story_id>')
def render_filled_form(story_id):

    user_stories = data_manager.get_data_from_file('stories.csv')

    return render_template('form.html', title="Edit Story", user_story=user_stories[int(story_id) - 1])


if __name__ == '__main__':
    app.run()
