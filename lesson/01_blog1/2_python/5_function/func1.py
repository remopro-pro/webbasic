# 用語の説明: ()の中の渡される変数を「引数」、returnで返ってくる値を「戻り値」という
def get_welcome_message(name):
    message = "ようこそ " + name + "さん"
    return message


msg = get_welcome_message("John")
print(msg)

# nameという変数は、get_welcome_messageの中だけで有効なので、以下はエラーになる
# print(name)
