
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