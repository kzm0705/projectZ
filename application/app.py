# pyapp/application/app.py

from flask import Flask
from flask import render_template


# Flaskアプリのインスタンスを作成
# static_folderとtemplate_folderのパスを明示的に指定
app = Flask(__name__, 
            static_folder='../static', 
            template_folder='../templates')

# ルーティング設定
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)