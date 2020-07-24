def add(a, b):
    return a + b


# 用語の説明: ↑のaddを「関数」、a, bを「引数」、returnで返ってくる値を「戻り値」という


def get_welcome_message(name):
    return "ようこそ " + name + "さん"


result = add(1, 2)
print(result)

msg = get_welcome_message("John")
print(msg)
