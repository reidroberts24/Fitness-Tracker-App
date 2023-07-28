from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash

@app.route('/food/dashboard')
def food_dashboard():
    return render_template('food_dashboard.html')