# Python Password Strength Checker 🔐

A Python-based cybersecurity project that analyzes sample passwords, identifies common weaknesses, and provides recommendations for improving password security.

## 📖 Project Overview

I developed this project as part of my transition into IT and cybersecurity while pursuing my B.S. in Cybersecurity and Information Assurance at Western Governors University.

The goal was to strengthen my Python programming skills while exploring password security concepts, input validation, and automated software testing.

The program started as a basic password length checker and evolved through four versions into an application with multiple security checks and automated unit tests.

## 🛠️ Features

- Checks for a minimum password length of 12 characters
- Identifies uppercase and lowercase letters, numbers, and special characters
- Detects passwords from a small built-in common-password list
- Identifies repeated characters and selected predictable patterns
- Provides feedback explaining potential password weaknesses
- Uses concealed input through Python's `getpass` module
- Allows users to evaluate multiple sample passwords in one session
- Includes eight automated unit tests

## 💻 Technologies Used

- **Python 3** — Application development
- **unittest** — Automated testing
- **getpass** — Concealed terminal input
- **GitHub** — Project documentation and version control

## 🚀 How to Run

1. Download or clone this repository.
2. Open Command Prompt or a terminal in the project folder.
3. Run:

```bash
python password_checker.py
```

4. Enter a fictional sample password.
5. Review the analysis and recommendations.
6. Type `quit` to exit.

## 🧪 Automated Testing

This project includes eight automated tests covering:

- Short passwords
- Common passwords
- Repeated characters
- Predictable patterns
- Passwords meeting all five basic checks
- Numeric-only passwords
- Empty inputs
- Uppercase letters and symbols

Run the tests using:

```bash
python -m unittest discover -v
```

**Verified test results:**

```text
Ran 8 tests in 0.027s

OK
```

All eight tests passed during local development.

## 🔒 Security Limitations

This application is intended for educational purposes and is not a production-grade password security assessment tool.

- The built-in common-password list is limited.
- It does not check comprehensive breached-password databases.
- It does not calculate reliable password entropy.
- Meeting all five basic requirements does not guarantee that a password is secure.
- Only fictional passwords should be used for testing.

## 📚 What I Learned

Through this project, I gained practical experience with:

- Python variables and data types
- Conditional statements and loops
- Functions and reusable code
- Lists, sets, and dictionaries
- String manipulation and Boolean logic
- Password security fundamentals
- Automated unit testing
- Troubleshooting Python programs
- GitHub repository management

## 👨‍💻 About Me

I'm Adam Jefferson, an educator transitioning into information technology and cybersecurity. I'm currently pursuing my B.S. in Cybersecurity and Information Assurance at Western Governors University.

This repository is part of my growing portfolio of hands-on technical projects.

**GitHub:** https://github.com/adamrjefferson
