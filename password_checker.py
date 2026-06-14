import re

name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Add more than 8 characters to your password")

if len(password) >= 12:
    score += 1

if re.search(r'[A-Z]', password):
    score += 1
else:
    feedback.append("Add an uppercase letter to your password")

if re.search(r'[a-z]', password):
    score += 1
else:
    feedback.append("Add a lowercase letter to your password")

if re.search(r'\d', password):
    score += 1
else:
    feedback.append("Add a number to your password")

if re.search(r'[!@#$%]', password):
    score += 1
else:
    feedback.append("Add symbols such as !@#$% to your password")

name_parts = name.split()
for part in name_parts:
    if part.lower() in password.lower():
        score -= 1 
        feedback.append("Your password contains part of your name")

if email.lower() in password.lower():
    score -= 1
    feedback.append("Your password is similar to your email")

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength:" , strength)
print("Feedback:")
for tip in feedback:
    print("-", tip)