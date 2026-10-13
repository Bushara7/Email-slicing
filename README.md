# Email-slicing
Email Username and Domain Extractor

A simple Python project that extracts the username and domain 
from an email address and checks whether the domain is supported.

📌 About the Project

The Email Username and Domain Extractor is a beginner-friendly Python project 
created to practice strings, conditional statements, loops, user input, and basic validation.

The program asks the user to enter an email address, separates the 
username from the domain, and displays the extracted information if the input passes its checks.

✨ Features
Extracts the username from an email address.
Extracts the domain from an email address.
Supports gmail.com and rediffmail.com.
Checks for a missing username or domain.
Handles input that does not contain exactly one @ symbol.
Repeats the input process until a supported email format is entered.
Uses only Python's built-in features.

🛠️ Technologies Used
Language: Python 3
Concepts: Strings, loops, conditionals, sets, functions, and string methods
Dependencies: None

📂 Project Structure
email-username-domain-extractor/
├── email_extractor.py
├── README.md


🚀 Getting Started
Prerequisites

Install Python 3 on your computer.

Download it from the official website:

https://www.python.org/downloads/

Installation
Clone this repository:
   git clone https://github.com/YOUR-USERNAME/email-username-domain-extractor.git

Navigate to the project directory:
   cd email-username-domain-extractor

Run the Python program:
   python email_extractor.py


On some systems, use:

   python3 email_extractor.py


Replace YOUR-USERNAME with your GitHub username.


💻 Example Usage
Valid input
Enter Email:
student@gmail.com
Username: student
Domain: gmail.com

Email details extracted successfully!

Missing username
Enter Email:
@gmail.com
Username is missing. Please try again.

Missing domain
Enter Email:
student@
Domain is missing. Please try again.

Unsupported domain
Enter Email:
student@yahoo.com
Invalid or unsupported domain!
Supported domains: gmail.com, rediffmail.com


🎯 Learning Objectives

This project demonstrates how to:

Take input from a user.
Manipulate strings in Python.
Find and split text using delimiters.
Apply if, continue, and break statements.
Use sets to store supported values.
Write and call a function.
Organize a small Python program.

⚠️ Limitations
Only gmail.com and rediffmail.com are supported.
The program performs basic input checks; it does not implement full email-address validation.
It does not verify whether an email account exists.
It does not send emails or connect to an email service.

🔮 Future Improvements
Support additional email domains.
Add more comprehensive email-format validation.
Allow the user to process multiple addresses.
Add automated unit tests.
Create a graphical user interface.

Created as a beginner Python project for learning and practicing programming fundamentals.

If you find this project useful for learning Python, feel free to fork the repository and improve it.
