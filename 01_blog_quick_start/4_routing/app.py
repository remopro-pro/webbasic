from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "こんにちは!"


@app.route("/page1")
def page1():
    return "ページ1"


@app.route("/page2/desu/yo")
def page2():
    return "ページ2"


@app.route("/users/<int:user_id>")
def show_user(user_id):
    return "ユーザーID: " + str(user_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
