from flask import Flask

app = Flask(__name__)   #Flaskクラスのインスタンス作成

#/というＵＲＬに対しての処理を追加
@app.route('/')
def index():
    return 'Hello world?'

#開発用サーバー実行
if __name__=='__main__':
    app.run(debug=True)