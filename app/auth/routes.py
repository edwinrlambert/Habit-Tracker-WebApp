from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.extensions import db
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

# Register Route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('habits.dashboard'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash("Account created! You can now login in.", "success")
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('habits.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('habits.dashboard'))
        else:
            flash("Invalid email or password", "danger")
        
    return render_template('auth/login.html', form=form)

# Logout Route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for('auth.login'))