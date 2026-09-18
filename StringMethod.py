# name = input("Enter your full name:")
# phone_number = input("Enter your phone number:")
# result1 = name.find("d")
# result2 = name.rfind("d")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")
# print (result1, result2)
# print (name)
# print(result)
# print(phone_number)
# print(help(str))

username = input("Enter your username:")
if len(username)>12:
    print("Username should be no longer than 12 characters.")
elif not username.find(" ") == -1:
        print("Username should not contain spaces.")
elif username.isalpha() is False:
    print("Username should not contain digits.")
else:
    print("Your username is valid.")
