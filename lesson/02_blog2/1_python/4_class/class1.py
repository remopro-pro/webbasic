class User:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age


user1 = User("磯野", "カツオ", 11)
user2 = User(last_name="磯野", first_name="ワカメ", age=9)

print(user1.first_name)

print(user2.last_name)

user1.age = 12
print(user1.age)
