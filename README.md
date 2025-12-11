# Create and get user
Test for requests: Create user, Get user on Pytest

Test create user with unique ID, username, email in format:<br/>
ID: current time + current date<br/>
username: random first name + ramdom last name + current time + current date<br/>
email: \<username\>@test.com

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:<br/>
   `git clone https://github.com/ritakolupaeva/create-and-get-user.git`

2. Open terminal in the folder with rerepository:<br/>
   `ls create-and-get-user`

3. Install virtual environment:<br/>
   `python3 -m venv .venv` # macOS<br/>
   `python -m venv .venv`  # Windows

4. Activate virtual environment:<br/>
   `source .venv/bin/activate`  # macOS<br/>
   `.venv\Scripts\activate.bat` # Windows

5. Install Pytest:<br/>
   `pip install pytest`

6. Install Faker:<br/>
   `pip install faker`

7. Check installation:<br/>
   `pytest --version`

8. Launch tests:<br/>
    `pytest -v -s`

9. Deactivate virtual environment:<br/>
   `deactivate`

## Additional information
If import requests is highlighted in yellow, click on it, select "Quick fix" and select the recommended Interpreter.

