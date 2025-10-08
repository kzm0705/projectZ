
from flask_sqlalchemy import SQLAlchemy
import pytz
from datetime import datetime



db = SQLAlchemy()

DB_INFO = {
    'user': 'postgres',
    'password': 'a1a2a3a4a5',
    'host' : 'localhost',
    'name' : 'postgres'
}
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://{user}:{password}@{host}/{name}'.format(**DB_INFO)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(850), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    tokyo_timzone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timzone))

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(200), nullable=False)
    recipe_image =db.Column(db.String(400), nullable=True)
    tokyo_timzone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timzone))


class images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path =db.Column(db.String(400), nullable=False)


class Recipe_temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(200), nullable=False)
    image_path = db.Column(db.String(400), nullable=False)
    tokyo_timzone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timzone))