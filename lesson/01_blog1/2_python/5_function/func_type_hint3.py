def get_user_age_message(name: str, age: int) -> str:
    return f"{name}さんは{age}歳です"


# Noneは存在しないことを表す
def show_user_age_message(name: str, age: int) -> None:
    print(f"{name}さんは{age}歳です")


msg = get_user_age_message("磯野", 18)
print(msg)

show_user_age_message("磯野", 18)
