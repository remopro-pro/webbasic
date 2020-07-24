# 戻り値（return）がない例
def show_welcome_message(name):
    print("ようこそ " + name + "さん")


# 引数がない例
def get_name():
    return 'John'


user_name = get_name()
print(user_name)

show_welcome_message(user_name)
