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
   `cd create-and-get-user`

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

7. Launch test:<br/>
    `pytest -v -s`

8. After launch test you can see results in terminal in format:<br/>
   `User created with...` with data from create user request<br/>
   `User received with...` with data from get user request<br/>

9. Deactivate virtual environment:<br/>
   `deactivate`

## Additional information
If `import requests` in `user_api.py` file will be underlined in yellow, move the mouse cursor over it in VS Code, select "Quick Fix...", then "Select a different interpreter" and select the recommended Interpreter.

