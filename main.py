# Import necessary libraries
import json
import os
import io
import psycopg2

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
@app.route('/test', methods=['GET', 'POST'])
def test():
    return "testing 123"

@app.route('/exclusive', methods=['GET', 'POST'])   
def exclusive():
    return render_template('exclusive.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def signup():
    return render_template('register.html')
@app.route('/recovery', methods=['GET', 'POST'])
def standard():
    return render_template('recovery.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)