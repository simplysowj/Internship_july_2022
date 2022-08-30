from ast import Raise
from logging import raiseExceptions
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import string
from flask import flash


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError
from wtforms.validators import InputRequired, Length,DataRequired
from flask_bcrypt import Bcrypt



app=Flask(__name__)
bcrypt = Bcrypt(app)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mykey'

db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
   
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    print(username)
    print(password)


class RegisterForm(FlaskForm):
  
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        x = User.query.filter_by(username='dj@gmail.com').first()
        print(x.username)
        existing_user_username = User.query.filter_by(username=username.data).first()
        print(existing_user_username)
        print(username.data)
        print(username)
        
        if existing_user_username:
            print('entered6') 
           
            raise ValidationError('Username already exists')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

class Urls(db.Model):
   
    id_ = db.Column("id_", db.Integer, primary_key=True)
    shortUrl = db.Column("shortUrl", db.String(5))
    longUrl = db.Column("longUrl", db.String())
    print(shortUrl)
    print(longUrl)
    def __init__(self, shortUrl, longUrl):
        self.shortUrl = shortUrl
        self.longUrl = longUrl
@app.before_first_request
def create_tables():
    db.create_all()

def shortenUrlUtil():
    allAlphabets = string.ascii_lowercase + string.ascii_uppercase
    while True:
        randAlphabets = random.choices(allAlphabets, k=5)
        randAlphabets = "".join(randAlphabets)
        shortUrl = Urls.query.filter_by(shortUrl=randAlphabets).first()
        if not shortUrl:
            return randAlphabets



@app.route('/url/<url>')
def displayUrl(url):
    print(url)
    return render_template('urlDisplay.html', generatedUrl = url,  urls=Urls.query.all())



@app.route('/url-shortening/<generatedUrl>')

def useShortUrl(generatedUrl):
    print(generatedUrl)
    originalUrl = Urls.query.filter_by(shortUrl=generatedUrl).first()
    
    if originalUrl:
        print('entered1')
        return redirect(originalUrl.longUrl)
    else:
        print('entered2')
        return '<h2>Url doesnt exist</h2>'




@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                 
                 return "password is incorrect"
           
    
    return render_template('login.html', form=form)



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if current_user.is_authenticated:
        if request.method == 'POST':
            url = request.form['urlInput']
            urlExists = Urls.query.filter_by(longUrl=url).first()
            if urlExists:
                #return corresponding shortURL
                return redirect(url_for("displayUrl", url = urlExists.shortUrl))
            else:
                #create a new short url
                shortURL = shortenUrlUtil()
                newUrl = Urls(shortURL, url)
                db.session.add(newUrl)
                db.session.commit()
                urlExists = Urls.query.filter_by(longUrl=url).first()
                return redirect(url_for("displayUrl", url = urlExists.shortUrl))
        else:
            return render_template('dashboard.html', urls = Urls.query.all())


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

 

if( __name__ == '__main__'):
        app.run(debug=True)