from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def top():
    return render_template("top.html")


@app.route('/articles')
def articles():
    return render_template("articles/index.html")


@app.route('/articles/<int:article_id>')
def show_article(article_id):
    return render_template("articles/show.html", article_id=article_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
