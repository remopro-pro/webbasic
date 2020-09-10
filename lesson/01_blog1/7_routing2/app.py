from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def top():
    return '<h1>トップページ</h1> <a href="/articles">記事一覧</a>'


@app.route('/articles')
def articles():
    return '<p><a href="/">トップに戻る</a></p> <h1>記事一覧ページ</h1> <ul><li><a href="/articles/1">記事1</a></li><li><a href="/articles/2">記事2</a></li></ul>'


@app.route('/articles/<int:article_id>')
def show_article(article_id):
    # f stringという機能を使っている
    return f'<p><a href="/">トップに戻る</a></p> <h1>記事詳細ページ</h1> 記事{article_id}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
