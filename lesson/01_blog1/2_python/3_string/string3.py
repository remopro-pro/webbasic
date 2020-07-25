name = "Mike"

# formatを使う
message = "ようこそ、{}さん".format(name)

# 表示して確認
print(message)

name2 = "Kate"
age = 18

# 複数の変数がある場合（数字もそのまま使える）
print("{}は、{}歳です".format(name2, age))
