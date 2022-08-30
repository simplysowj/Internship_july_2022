
import os
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key="Secret Key"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app,db)

class Data(db.Model):
    __tablename__="contacts"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    phone= db.Column(db.String(100))
   
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone =phone
  
@app.route("/", methods=['GET','POST'])
def home():
    all_data=Data.query.all()

    return render_template("index.html",contacts=all_data)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")

        my_data=Data(name,email,phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Contact Added Successfully")

    return redirect (url_for('home'))
@app.route('/update' , methods=['GET','POST'])
def update():
    if request.method=='POST':
        my_data=Data.query.get(request.form.get('id'))

        my_data.name=request.form['name']
        my_data.email = request.form['email']
        my_data.phone=request.form['phone']

        db.session.commit()
        flash("contact updated successfully")

        return redirect(url_for('home'))

@app.route('/delete/<id>/' , methods=['GET','POST'])
def delete(id):
   
        my_data=Data.query.get(id)

        db.session.delete(my_data)
        db.session.commit()
        flash("contact deleted successfully")

        return redirect(url_for('home'))

@app.route("/search",methods=['GET','POST'])
def search():
    if request.method=='POST':
        name = request.form.get("name1")
        search_data = Data.query.filter_by(name=name).first()
        print("search data is") 
        print(search_data)
        return render_template("search.html",input1=search_data)
        

if __name__=="__main__":
    app.run(debug=True,port=5000)
