from flask import render_template
from app import app

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
