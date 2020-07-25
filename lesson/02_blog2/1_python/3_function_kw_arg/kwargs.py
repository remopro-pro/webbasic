def func1(name, age, job):
    print(f"{name}, {age}, {job}")


func1("磯野", 20, "Webエンジニア")


def func2(name, options):
    print(name)
    print(options)


func2("磯野", {"age": 20, "job": "Webエンジニア", "first_name": "カツオ"})


def func3(name, **options):
    print(name)
    print(options)


func3("磯野", age=20, job="Webエンジニア", first_name="カツオ")
