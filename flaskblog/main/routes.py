from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)

posts = [
    {
        'author': 'A',
        'title': 'Post 1',
        'content': 'My content 1st post',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'B',
        'title': 'Post 2',
        'content': 'My content 2nd post',
        'date_posted': 'April 2, 2022'
    }
]


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')