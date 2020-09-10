class User:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def get_full_name(self):
        return self.last_name + " " + self.first_name


user1 = User(last_name="磯野", first_name="カツオ", age=11)

name = user1.get_full_name()
print(name)
