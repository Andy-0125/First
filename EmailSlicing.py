email = input("Enter your email:")
username = email[:email.index("@", 0, 100)]
domain = email[email.index("@", 0, 100)+1:]
print(f"Your username is {username} and your domain is {domain}.")
