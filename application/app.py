# pyapp/application/app.py

from flask import Flask
from flask import render_template,request,redirect

from flask_sqlalchemy import SQLAlchemy
import pytz
from datetime import datetime

from db import db, Post
from init import app

# ルーティング設定
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    posts = Post.query.all()
    return render_template('admin.html', posts=posts)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_post = Post(title=title, body=body)
        try:
            db.session.add(new_post)
            db.session.commit()
            return redirect('/admin')
        except Exception as e:
            return f"An error occurred while adding the post: {e}"
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        try:
            db.session.commit()
            return redirect('/admin')
        except Exception as e:
            return f"An error occurred while updating the post: {e}"
    return render_template('edit.html', post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/admin')
    except Exception as e:
        return f'An error occurred while deleting the post: {e}'

# if __name__ == "__main__":
#     app.run(debug=True)