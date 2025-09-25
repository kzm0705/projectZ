# pyapp/application/app.py

from flask import Flask
from flask import render_template

from flask_sqlalchemy import SQLAlchemy
import pytz
from datetime import datetime

# Flaskアプリのインスタンスを作成
# static_folderとtemplate_folderのパスを明示的に指定
app = Flask(__name__, 
            static_folder='../static', 
            template_folder='../templates')

# dbの設定
db = SQLAlchemy()
DB_INFO = {
    'user': 'postgres',
    'password': 'a1a2a3a4a5',
    'host' : 'localhost',
    'name' : 'postgres'
}

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg://{user}:{password}@{host}/{name}'.format(**DB_INFO)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(850), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    tokyo_timzone = pytz.timezone('Asia/Tokyo')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tokyo_timzone))

# ルーティング設定
@app.route("/")
def index():
    return render_template('index.html')



# if __name__ == "__main__":
#     app.run(debug=True)