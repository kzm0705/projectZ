from flask import Flask

from db import db,SQLALCHEMY_DATABASE_URI
from flask_migrate import Migrate

#flaskアプリのインスタンス化,

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')

# dbの設定
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db.init_app(app)
migrate = Migrate(app,db)
# with app.app_context():
#     db.create_all()