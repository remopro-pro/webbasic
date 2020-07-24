from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # PyCharmで黄色くなるが、このlessonの構造のせいなので気にしない
    return render_template('top.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
