# Import necessary libraries
import json
import os
import io
import psycopg2
import datetime

from flask import Flask,render_template, request, jsonify,flash,url_for,redirect,session,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


# Initialize Flask application
app=Flask(__name__)

# Set Flask application configurations
app.config['SECRET_KEY']='david'
app.config['UPLOAD_FOLDER']='static/files'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres://avnadmin:AVNS__KRy1EHWDbCl4_XPVlF@corpshaven1-owamagbedavid-db8a.d.aivencloud.com:24798/defaultdb?sslmode=require'
db=SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100),unique=True, nullable=False)
#     phone_number = db.Column(db.Integer,unique=True, nullable=False)
#     service_year = db.Column(db.Integer, nullable=False)
#     batch = db.Column(db.String(1), nullable=False)
#     stream = db.Column(db.Integer, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     account_type = db.Column(db.String(20), nullable=False)"
# # Define User model
# class User(db.Model):
#     __tablename__ = 'users'

#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(100), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.Enum('corper', 'property owner', 'admin'), nullable=False)

# # Define Property model
# class Property(db.Model):
#     __tablename__ = 'properties'

#     property_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     location = db.Column(db.String(255), nullable=False)
#     rent_amount = db.Column(db.Numeric(10, 2), nullable=False)
#     amenities = db.Column(db.Text, nullable=True)

# # Define InspectionRequest model
# class InspectionRequest(db.Model):
#     __tablename__ = 'inspection_requests'

#     request_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     request_datetime = db.Column(db.DateTime, nullable=False)

# # Define Review model
# class Review(db.Model):
#     __tablename__ = 'reviews'

#     review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     rating = db.Column(db.Integer, nullable=False)
#     comment = db.Column(db.Text, nullable=True)

# Define the homepage route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():

   # Render the homepage template for GET requests
    return render_template('index.html')




@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')


@app.route('/singleproperty', methods=['GET', 'POST'])   
def exclusive():
    return render_template('property-single.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        if len(email) > 4:
            flash('First name must be greater than 1 character.', category='error')
    
    

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
            first_name=request.form.get("first_name")
            last_name=request.form.get("last_name")
            email = request.form.get("email")
            phone_number = request.form.get("phonenumber")
            year = request.form.get("year")
            batch = request.form.get("batch")
            stream = request.form.get("stream")
            password = request.form.get("psw")
            confirm_password = request.form.get("confirm_password")
            account_type = request.form.get("account_type")
                
                #Validation
            errors=[]
            if len(email) < 4:
                   flash('Email must be greater than 3 characters.') 
            elif not (email.endswith('@gmail.com') or email.endswith('@yahoo.com') or email.endswith('@outlook.com')):
                flash("Email must be either @gmail.com, @yahoo.com, or @outlook.com", "error")
                
 
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 1 character.', category='error')
            elif len(phone_number) != 11 or not phone_number.isdigit():
                flash("Phone number must be 11 digits.", "error")
               
            current_year = datetime.datetime.now().year
            if int(year) < current_year - 1 or int(year) > current_year:
                flash(f"Service year must be between {current_year - 1} and {current_year}", "error")
                
            
            elif len(password) < 8:
                flash('Password must be at least 8 characters.', category='error')
            elif confirm_password != password:
                 flash('Passwords don\'t match.', category='error')
            elif not account_type:
                flash("Please select an account type.", "error")
               
            elif not batch:
                flash("Please select a batch.", "error")
                
            elif not stream:
                flash("Please select a stream.", "error")
                
            else:
                 flash('Account created!', category='success')
                 return redirect(url_for('register'))
        
           
    return render_template('register.html')

@app.route('/recovery', methods=['GET', 'POST'])
def standard():
    return render_template('recovery.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        email = request.form.get("email")
        if len(email) > 4:
            flash('First name must be greater than 1 character.', category='error')
    return render_template('test.html',category='error')
if __name__ == '__main__':
    app.run(debug=True)