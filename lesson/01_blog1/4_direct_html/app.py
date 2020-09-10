from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><title>私のプログラミング学習ブログ</title></head><body><h1>私のプログラミング学習ブログ</h1><div>プログラミングで学んだことを記録していくブログ。</div><img src="static/images/character_program_happy.png" alt="トップ画像" width="200" height="200" /><h2>最新記事</h2><p><a href="index.html">記事一覧</a></p><table><thead><tr><th>投稿日</th><th>キーワード</th><th>タイトル</th></tr></thead><tbody><tr><td>2022/07/11</td><td><code>Python</code></td><td><a href="1.html">Pythonの小技</a></td></tr><tr><td>2022/07/08</td><td><code>Go</code></td><td><a href="">Go面白くなってきた</a></td></tr><tr><td>2022/07/06</td><td><code>MySQL</code> <code>Python</code></td><td><a href="">PythonからMySQLを使う</a></td></tr></tbody></table><p><a href="index.html">記事一覧</a></p></body></html>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
