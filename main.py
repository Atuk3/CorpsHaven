# Import necessary libraries
import json
import os
import io
from flask import Flask,render_template, request, jsonify,flash,url_for,redirect,session,make_response

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


# Initialize Flask application
app=Flask(__name__)

# Set Flask application configurations
app.config['SECRET_KEY']='david'
app.config['UPLOAD_FOLDER']='static/files'



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
def rooms():
    return render_template('services.html')
@app.route('/executive', methods=['GET', 'POST'])
def executive():
    return render_template('executive.html')

@app.route('/exclusive', methods=['GET', 'POST'])   
def exclusive():
    return render_template('exclusive.html')

@app.route('/standard', methods=['GET', 'POST'])
def standard():
    return render_template('standard.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('dashboard.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)