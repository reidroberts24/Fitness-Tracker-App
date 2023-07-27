from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('register_and_login.html')