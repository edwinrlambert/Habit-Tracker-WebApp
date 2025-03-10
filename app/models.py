from .extensions import db
from flask_login import UserMixin
from datetime import datetime

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utc)
    
    habits = db.relationship('Habit', backref='user', lazy=True)
    
    def __repr__(self):
        return f"<User: {self.username}>"
    
# Habit Model
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    frequency = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, default=datetime.timezone.utc)
    end_date = db.Column(db.Date, nullable=True)
    
    logs = db.relationship('HabitLog', backref='habit', lazy=True)
    
    def __repr__(self):
        return f"<Habit: {self.title}>"
    
# Habit Log Model
class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.timezone.utc, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Incomplete")
    
    def __repr__(self):
        return f"<HabitLog: {self.habit_id} on {self.date}>"