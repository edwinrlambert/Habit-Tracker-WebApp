from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    habits = db.relationship('Habit', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User: {self.username}>"
    
# Habit Model
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    frequency = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, default=datetime.now(timezone.utc))
    end_date = db.Column(db.Date, nullable=True)
    
    logs = db.relationship('HabitLog', backref='habit', lazy=True)
    
    def __repr__(self):
        return f"<Habit: {self.title}>"
    
# Habit Log Model
class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.now(
        timezone.utc), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Incomplete")
    
    def __repr__(self):
        return f"<HabitLog: {self.habit_id} on {self.date}>"