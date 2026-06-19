Password Strength Checker
A Python tool designed to help everyday users create stronger, more secure passwords. It evaluates passwords against key security criteria including length, use of numbers and symbols, and checks that the password doesn’t contain personal information like your name or email. It also estimates how long it would take a hacker to crack your password, and gives personalized feedback to help you improve it.

Features
	•Checks for uppercase and lowercase letters
	•Checks for numbers
	• Checks for symbols (!@#$%)
	•Detects if password contains your name or email
	•Checks against a list of commonly used passwords
	•Estimates how long it would take a hacker to crack your password
	•Gives personalized feedback to help you improve your password

How to Run
	1.	Make sure you have Python installed on your computer (latest version recommended) — download it at python.org if you don’t have it
	2.	Download the password_checker.py file from this repository
	3.	Open your terminal, navigate to the folder where you saved the file, and run:
python password_checker.py 
  4. Follow the prompts — enter your name, email, and password when asked!

What I Learned
Building this project taught me that a password can appear mathematically strong — with a huge number of possible combinations — but still be weak if it contains common words or patterns. This is the difference between brute force attacks (trying every possible combination) and dictionary attacks (trying common words and patterns first). Real security tools need to defend against both, which is why I built both a crack time estimator AND a common password blacklist.
I also learned the importance of debugging with real test cases. For example, I discovered that checking if a name was “in” a password failed for people with two part names like “Dylan Medina” — because the full string “Dylan Medina” wasn’t inside the password, but “Dylan” was. Fixing that taught me to always think about edge cases and real world input, not just ideal scenarios.
