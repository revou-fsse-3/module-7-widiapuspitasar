# Revou Asignment Module 7

## My User Dummy
    1. Not Admin
        email: dummy@gmail.com
        passsword: dummy
    2. Admin
        email: revou123@gmail.com
        password: revou123

## Shortcut localhost:
    Home: http://127.0.0.1:5000
    Login: http://127.0.0.1:5000/login
    Register: http://127.0.0.1:5000/register
    Product:  http://127.0.0.1:5000/product


## Flask User Authentication Project

This Flask project is designed to showcase user authentication using either session-based or token-based authentication methods. The project includes a MySQL database to store user data securely.

## Database Setup

1. **Create MySQL Database:**
   - Create a new MySQL database for this project.

2. **Design Database Tables:**
   - Design and implement database tables to store user data, including fields such as username, email, and securely hashed passwords.

## Flask Application & Dependencies

3. **Set Up Flask Application:**
   - Initialize a new Flask application.

4. **Install Dependencies:**
   - Install the following dependencies using `pip install`:
     - Flask
     - SQLAlchemy
     - Flask-Login (for session-based authentication)
     - Flask-JWT-Extended (for token-based authentication)
     - MySQL Connector Python (for connecting to MySQL)

## Database Connection

5. **Configure Database Connection:**
   - Configure your Flask application to connect to the MySQL database using the connection URI.

## Model Creation

6. **Create Model File:**
   - Create a model file representing the user data structure using SQLAlchemy.
   - Define fields for username, email, and password (hashed securely using a hashing algorithm like bcrypt).

## Data Fetching and Display

7. **Fetch and Display User Data:**
   - Fetch all user data from the database.
   - Display the user data in a well-formatted table on a web page.

## Authentication Method (Choose One)

### Session-Based Authentication

8. **Implement Session-Based Authentication:**
   - Utilize Flask-Login for user session management.
   - Implement user login and logout functionalities.
   - Securely store user information in sessions.
   - Protect specific routes requiring user authentication.


## Contributing

If you want to contribute to this project, please fork the repository and submit pull requests with your changes.

## License

This project is licensed under the [MIT License](LICENSE).