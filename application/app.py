# pyapp/application/app.py

from flask import Flask
from flask import render_template,request,redirect, url_for
from werkzeug.utils import secure_filename

from db import db, Post, images, Recipe_temp
from init import app
from image_module.save_image import save_image

import os
from PIL import Image

basedir = os.path.abspath(os.path.dirname('static'))

UPLOAD_FOLDER = os.path.join(basedir, 'static', 'images')

# ルーティング設定
@app.route("/")
def index():
    return render_template('index.html')

#READ
@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    recipes = Recipe_temp.query.all()
    return render_template('gallery.html', Recipe_temp=recipes)

#CRUDのC
@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        #SQL処理
        recipe_name = request.form['recipe_name']
        if 'file' not in request.files or request.files['file'].filename == "":
            return render_template('upload.html', msg="ファイルが選択されていません。")
        
        save_image(request.files['file'], recipe_name=recipe_name)

        return redirect(  url_for('gallery') )
    return render_template('create.html')

#UPDATE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        try:
            db.session.commit()
            return redirect(url_for('gallery'))
        except Exception as e:
            return f"An error occurred while updating the post: {e}"
    return render_template('edit.html', post=post)
#DELETE
@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('gallery')
    except Exception as e:
        return f'An error occurred while deleting the post: {e}'

@app.route('/feeling')
def feeling():
    return render_template("feeling.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        print(f'created folder: {UPLOAD_FOLDER}')

    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == "":
            return render_template('upload.html', msg="ファイルが選択されていません。")
        
        image_path = request.files['file']
        # セキュアなファイル名にへんこう
        file_name = secure_filename(image_path.filename)
        #絶対パス作成
        full_path = os.path.join(UPLOAD_FOLDER, file_name)

        try:
            img =  Image.open(image_path)
            img.save(full_path ,format='PNG')
            #dbに保存するパス
            db_image_path = os.path.join('static', 'images', file_name)

            new_image = images(image_path=db_image_path)

            db.session.add(new_image)
            db.session.commit()
            
            return render_template('upload.html', context={ 'image_path' : image_path, 'msg':"アップロードできました"})

        except Exception as e:
            return f'An error occurred while adding the image: {e}'
        
    #画像一覧取得
    image = images.query.all()

    return render_template('upload.html', img_li=image)



