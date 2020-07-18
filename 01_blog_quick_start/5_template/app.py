from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "こんにちは!"


@app.route('/users')
def users():
    return "<h1>ユーザー一覧</h1><ul><li><a href='/users/1'>鈴木</a></li><li><a href='/users/2'>山田</a></li></ul>"


@app.route('/users/<int:user_id>')
def show_user(user_id):
    return "ユーザーID: " + str(user_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
