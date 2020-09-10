user = {"name": "磯野", "age": 18}

print(user)

print(user["name"])
print(user["age"])

# 以下はエラーになる
# print(user["job"])

print(user.get("name"))
print(user.get("age"))
# 以下はエラーにならず、Noneが返る
print(user.get("job"))
