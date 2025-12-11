# Create and get user
Test for requests: Create user, Get user on pytest

Test create user with unique ID, username, email in format:<br/>
ID: current time + current date
username: random first name + ramdom last name + current time + current date
email: <username>@test.com

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:<br/>
   `git clone https://github.com/ritakolupaeva/create-and-get-user.git`

2. Install virtual environment:<br/>
   `python3 -m venv .venv` # macOS<br/>
   `python -m venv .venv`  # Windows

3. Activate virtual environment:<br/>
   `source .venv/bin/activate`  # macOS<br/>
   `.venv\Scripts\activate.bat` # Windows

4. Install Pytest:<br/>
   `pip install pytest`

5. Install Faker:<br/>
   `pip install faker`

6. Check installation:<br/>
   `pytest --version`

7. Launch tests:<br/>
    `pytest -v -s`

8. Deactivate virtual environment:<br/>
   `deactivate`

## Additional information
If import requests is highlighted in yellow, click on it, select "Quick fix" and select the recommended Interpreter.

