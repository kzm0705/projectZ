# pyapp/application/app.py

from flask import Flask
from flask import render_template,request,redirect, url_for
from werkzeug.utils import secure_filename
from sqlalchemy.orm import joinedload

from db import db, Post, images, Recipe_temp, Ingredients_temp, Steps
from init import app
from image_module.save_image import save_image
from db_module.create_ingre_recipe import create_ingredient_recipe_query, crate_steps_query


import os
from PIL import Image
import re

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
    if request.method =='POST':
        recipe_name = request.form['recipe_name']
        number_of_people = request.form['number-of-people']
        array_data = {}
        #材料と分量と手順それぞれのリストを作り対応するクエリを作成しコミット
        for k in request.form.keys():
            if re.match(r'.+\[\]', k):
                array_key = k.replace('[]', '')
                array_data[array_key] = request.form.getlist(k)
        create_ingredient_recipe_query(id,array_data)
        crate_steps_query(id, array_data)

        return redirect(  url_for('gallery'))
    
    recipe = Recipe_temp.query.get_or_404(id)
    recipe.image_path = recipe.image_path.replace('static\\','').replace('\\', '/')

    return render_template('edit.html', recipe=recipe)

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
    

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = Recipe_temp.query.options(
        joinedload(Recipe_temp.Ingredients_temp),
        joinedload(Recipe_temp.Steps)
    ).get_or_404(id)
    recipe.image_path = recipe.image_path.replace('static\\','').replace('\\', '/')
    # print(f'----レシピデータ-----')
    # print(f'料理名:{recipe.recipe_name}; ID : {recipe.id}')
    # print(f'{recipe.num_people}人分のレシピです')

    # print("-----食材リスト------")
    # if recipe.Ingredients_temp:
    #     for ing in recipe.Ingredients_temp:
    #         # モデルの属性名（例: name, amount）を使って出力
    #         print(f"  - {ing.ingredient_name}: {ing.amount}")
    # else:
    #     print("  - 食材データなし")

    # # 📝 手順リストの出力
    # print("\n--- 手順リスト ---")
    # if recipe.Steps:
    #     # loop.index のように、enumerateで順番を付けて出力
    #     for index, flow in enumerate(recipe.Steps):
    #         # モデルの属性名（例: description）を使って出力
    #         print(f"  {index + 1}. {flow.description}")
    # else:
    #     print("  - 手順データなし")
    # print("-------------------------")
    # # ingredients = Ingredients_temp.query.get_or_404(id)
    # # steps = Steps.query.get_or_404(id)
    return render_template('recipe.html', recipe=recipe)

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
            db_image_path = os.path.join('images', file_name)

            new_image = images(image_path=db_image_path)

            db.session.add(new_image)
            db.session.commit()
            
            return render_template('upload.html', context={ 'image_path' : image_path, 'msg':"アップロードできました"})

        except Exception as e:
            return f'An error occurred while adding the image: {e}'
        
    #画像一覧取得
    image = images.query.all()

    return render_template('upload.html', img_li=image)



