from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('input.html')

@app.route('/second')
def second():
    return "<h1>Second Page</h1>"


@app.route('/posts/<string:postname>')
def single_post(postname):
    return f'The post is about {postname}'

def do_the_login():
    return (
        "<div>This is for the login</div>"
    )
def show_the_login_form():
    return (
        "<div>Here do th elogin </div>"
    )

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

@app.route('/shortenurl',methods=['GET','POST'])
def shorten_url():

    return render_template('shortenurl.html',shortcode=request.form['url'])