from flask import Blueprint, render_template, request,Flask, redirect,flash, url_for, render_template,request,session
from flask_login import login_required, current_user
from .models import User, details
from . import db 
import csv


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html", user=current_user)

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html", user=current_user)

@views.route('/disease', methods=['GET', 'POST'])
def disease():
    return render_template("doctor.html", user=current_user)
@views.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html", user=current_user)
@views.route('/profile-edit', methods=['GET', 'POST'])
def profileedit():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        diseases = request.form.get('diseases')
        city = request.form.get('location')
        address = request.form.get('address')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        new_user = details(email=email, fname=fname,lname=lname, diseases=diseases, city=city, address=address,phone=phone, dob=dob)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        flash('Details Updated', category='success')
        return redirect(url_for('views.profile'))

    return render_template("profileedit.html", user=current_user)



