def get_age(age):
    return age


my_age = get_age(14)  
print("Your age is:", my_age)


def user_info(first_name, last_name, age, address):
    return f"Hello {first_name} {last_name}, you are {age} years old and you live in {address}."


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

info = user_info(first_name, last_name, age, address)
print(info)


