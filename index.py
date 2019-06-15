from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, SigninForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '*&H)#($)JDOMOM#$@)S'
posts = [
    {
        "name":'daniel',
        "title":'Unsung Heroes',
        "song":" If your current network has https://www.anaconda.com blocked, please file a support request with your network engineering team.  "
    },
    {
        "name":'Ruth',
        "title":'Missing Shoes',
        "song":"An HTTP error occurred when trying to retrieve this URL. HTTP errors are often intermittent, and a simple retry will get you on your way."
    }
]

@app.route("/")
@app.route("/home")
def home():
    return  render_template('home.html',posts=posts,title='Blog List')

@app.route("/about")
def about():
    return render_template('about.html',title='About Us')

@app.route('/register',methods= ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/signin')
def signin():
    form = SigninForm()
    return render_template('signin.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
