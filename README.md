# harvardstolendataproject
### Setup
After cloning the repo, you will need to set up a virtual environment for the backend. 
Open up a new terminal inside the server directory. Run `virtualenv venv` to create the virtual environment.
Before continuing, activate the virtual environment (the specific command to do this varies by OS and can be googled).
Once the virtual environment is activated, run `pip install -r requirements.txt` in the server directory. 
To start the backend server, run `py app.py` (or `python3 app.py` for non-windows OS).

To start the frontend server, open a new terminal and navigate to the client directory. Run `npm run serve`.
Navigate to http://localhost:8080/home to see the website.
Login is handled at http://localhost:8080/login and once logged in articles can be added at http://localhost:8080/add-article.
The login credentials are `username: mark` and `password: testpass`.
The login and add article interfaces are a little jank, but they are functional.
Once you log in you will be logged in for 30 minutes, and then the session will expire and you will have to login again.

If you have any questions, concerns, errors, ... just email me (mpekala@college.harvard.edu)
