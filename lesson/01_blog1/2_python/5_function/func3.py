def show_user_age_message(name, age):
    print(f"{name}さんは{age}歳です")


show_user_age_message("Kate", 17)

show_user_age_message(name="Kate", age=17)

show_user_age_message("Kate", age=17)

# これはできない
#show_user_age_message(name="Kate", 17)

show_user_age_message(age=17, name="Kate")
