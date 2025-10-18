import os

from db import db,Recipe_temp

from image_module.save_image import basedir


def remove_image(path):
    full_path = os.path.join(basedir,'static', path).replace('/',"\\")
    try:
        os.remove(full_path)
    except Exception as e:
        return print(e)



