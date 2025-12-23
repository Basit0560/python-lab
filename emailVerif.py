# Write a program to check the validity of an email ID.

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
