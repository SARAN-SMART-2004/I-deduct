from flask import Blueprint, render_template, request,Flask, redirect, url_for, render_template,request,session
from flask_login import login_required, current_user
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
def profile():
    return render_template("profileedit.html", user=current_user)



