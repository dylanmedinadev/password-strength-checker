import re
import hashlib
import requests

def check_breach(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 = sha1_password[:5]
    rest = sha1_password[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    hashes = response.text.splitlines()
    for h in hashes:
        hash_value, count = h.split(":")
        if hash_value == rest:
            return int(count)
    return 0

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
        if "Your password contains part of your name" not in feedback:
            feedback.append("Your password contains part of your name")

if email.lower() in password.lower():
    score -= 1
    feedback.append("Your password is similar to your email")

common_passwords = ["password", "123456", "qwerty", "password1", "admin", "letmein"]
for word in common_passwords:
    if word in password.lower():
        score -= 1
        if "This is a commonly used password and is very easy to guess" not in feedback:
            feedback.append("This is a commonly used password and is very easy to guess")

pool = 0
if re.search(r'[a-z]', password):
    pool += 26
if re.search(r'[A-Z]', password):
    pool += 26
if re.search(r'\d', password):
    pool += 10
if re.search(r'[!@#$%]', password):
    pool += 32

combinations = pool ** len(password)
seconds = combinations / 1_000_000_000

if seconds < 60:
    crack_time = "less than a mintue"
elif seconds < 3600:
    crack_time = "a few mintues"
elif seconds < 86400:
    crack_time = "a few hours"
elif seconds < 31536000:
    crack_time = "a few days"
else:
    crack_time = "years or longer"
print("Estimated crack time:", crack_time)

breach_count = check_breach(password)
if breach_count > 0:
    score -= 3
    feedback.append(f"This password has been seen in {breach_count} data breaches!")
else:
    feedback.append("Good news! This password was not found in any known data breaches.")

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