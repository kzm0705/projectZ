import os
from PIL import Image

from db import db,Recipe_temp

basedir = os.path.abspath(os.path.dirname('static'))
UPLOAD_FOLDER = os.path.join(basedir, 'static', 'images')

def save_image(file_name, recipe_name=None):
    
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    full_path = os.path.join(UPLOAD_FOLDER, file_name.filename)

    try:
        img = Image.open(file_name)
        img.save(full_path, format='PNG')
                #dbに保存するパス
        db_image_path = os.path.join('static', 'images', file_name.filename)

        new_image = Recipe_temp(image_path=db_image_path, recipe_name=recipe_name)

        db.session.add(new_image)
        db.session.commit()

    except Exception as e:
        return print(f'An error occurred while saving the image: {e}')
    
    print(f'絶対パス:{full_path}')
    print(f'DB保存パス: {db_image_path}')