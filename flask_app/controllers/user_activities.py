from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash

@app.route('/activity/dashboard')
def activity_dashboard():
    return render_template('activity_dashboard.html')