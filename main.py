from flask import Flask
from flask import render_template
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    posts = [ # список выдуманных постов
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/data', methods=['POST'])
def getData():
    print(request.json)
    return "Successful"


@app.route('/user/')
@app.route('/user/<username>')
def userProfile(username = None):
    if username:
        return f"User ID : {username}"    
    return f"User undefined"

if __name__ == "__main__":
    app.run(debug=True)