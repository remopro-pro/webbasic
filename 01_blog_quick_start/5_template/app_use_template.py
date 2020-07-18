from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "こんにちは!"


@app.route('/users')
def users():
    return render_template("users/index.html")


@app.route('/users/<int:user_id>')
def show_user(user_id):
    return render_template("users/show.html", id=user_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
