import json


def filter_users_by_name(name):
    """filters the user data by name and displays the results"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """filters the user data by age and displays the results"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """filters the user data by email and displays the results"""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name, age, emial): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: "))
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Wrong input.")
    elif filter_option in ["email", "e-mail"]:
        email_to_search = input("Enter an e-mail address to filter users: ").strip().lower()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")