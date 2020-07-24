# 代入
name = "鈴木"  # 文字列（str）
age = 20      # 整数（int）

# 表示
print(name)
print(age)

# 文字列（str）の結合
print("鈴木" + "さん")
print(name + "さん")

# strとintは結合できないので、以下はエラーになる
#print(name.py + "さんは、" + age + "歳です")

age_str = "20"  # stringの「20」
# age_strはintではなくstrなので、結合できる
print(name + "さんは、" + age_str + "歳です (1)")

# age（int）をstrに変換して結合
print(name + "さんは、" + str(age) + "歳です (2)")
