from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Post
from . import db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        post = request.form.get('post')

        if post is None:
            flash('The Post is None', category='error')
        elif len(post) < 19:
            flash('Post must be at least 20 characters long!', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post Added!', category='success')

    return render_template("home.html", user=current_user)

