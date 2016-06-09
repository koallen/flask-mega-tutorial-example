from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Shawn'} # a fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Rainy day in Singapore.'
        },
        {
            'author': {'nickname': 'Mike'},
            'body': 'I\'ll watch the new movie tomorrow.'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
