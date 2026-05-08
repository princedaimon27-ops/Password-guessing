Password Guessing Program
Description

This is a simple Python password guessing program created using Python in Visual Studio Code.
The program allows a user to enter a password with a maximum of 3 attempts.

If the correct password is entered, access is granted.
If the user fails after 3 attempts, access is denied.

Features
Password authentication
Limited login attempts
Displays wrong password messages
Denies access after maximum attempts
Technologies Used
Python
Visual Studio Code
Code Overview
# simple password check
correct_password = "Golden"
attempts = 0
max_attempts = 3
password = ""

while attempts < max_attempts and password != correct_password:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted")

    if password != correct_password:
        attempts += 1
        print(f"Wrong password X({attempts}/{max_attempts})")

if attempts >= max_attempts:
    print("Too many attempts. Access denied")
How It Works
The program stores the correct password.
The user is asked to enter a password.
If the password is correct:
"Access granted" is displayed.
If the password is incorrect:
The attempt counter increases.
The user is informed of the remaining attempts.
After 3 failed attempts:
"Too many attempts. Access denied" is displayed.
