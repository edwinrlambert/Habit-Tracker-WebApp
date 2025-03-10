from flask import Blueprint, render_template

habits = Blueprint('habits', __name__)

@habits.route('/')
def dashboard():
    return "<h1> Welcome to the Habit Tracker Dashboard!</h1>"