Author - Leeroy Mokua Ondieki (email - leeroynyanchwa@gmail.com)


Front-End
The web_dynamic directory defines the Front-End of the Mingle application. I use the Flask framework from Python to achieve this. I choose Flask because it is easy and simple to set up a project and get running, making it easier to focus on the ideas of the project.

Structure of the Front-End
The Front-End is organized into several key components:

Templates: The HTML files that make up the user interface are stored in the templates/ directory. These templates are rendered by Flask and often make use of Jinja2 for dynamic content.

Static Files: The static/ directory contains all the static assets such as CSS files, JavaScript files, and images. These assets help in styling and adding interactivity to the HTML templates.

Forms: Custom forms, such as login and registration forms, are defined in forms.py. Flask-WTF is used to manage form validation and handling.

Routes: The various routes or endpoints that the Flask application handles are defined in the Python files within web_dynamic/. These routes correspond to different pages of the Mingle application, such as the homepage, user profile, and more.

Why Flask?
Ease of Use: Flask’s minimalistic design allows for rapid development, letting me focus more on the project’s functionality and user experience rather than the framework's complexities.

Flexibility: Flask is unopinionated and gives the freedom to structure the application as needed. This flexibility was crucial in adapting the Front-End to the specific needs of the Mingle application.

Extensibility: With Flask, it’s straightforward to integrate additional libraries and tools that enhance the Front-End. This includes extensions for form handling, security, and connecting with the Back-End.

Responsive Design
The Front-End is designed to be responsive, ensuring that the Mingle application works well on different devices, including desktops, tablets, and smartphones. CSS media queries are used extensively to achieve this.

Interactive Features
The application includes interactive features powered by JavaScript and AJAX. These features improve the user experience by enabling real-time updates without needing to reload the page.

Future Enhancements
In future iterations, the Front-End might be further enhanced by integrating modern JavaScript frameworks like React or Vue.js, which would allow for more dynamic and component-based UIs.

Backend
The backend of this application is built with Flask, SQLAlchemy, and Flask-RESTful, handling the API requests and managing the database. The project is structured into different modules and follows a clear object-relational mapping (ORM) model with SQLAlchemy, making it easy to manage and manipulate data. Below is an overview of the backend components.

Models
*BaseModel
The BaseModel class is the foundation for all other models in the application. It includes the basic attributes and methods shared by all models, such as id, created_at, and updated_at. This class also handles the initialization, saving, and deletion of objects from the database.

Attributes:

id (String): A unique identifier for each record.
created_at (DateTime): The timestamp when the record was created.
updated_at (DateTime): The timestamp when the record was last updated.
Methods:

__init__: Initializes a new instance of the model, setting default values for attributes if not provided.
save: Updates the updated_at attribute and saves the instance to the database.
to_dict: Converts the instance into a dictionary format, which is useful for JSON serialization.
delete: Removes the instance from the database.
*User
The User model represents users within the application. It extends the BaseModel and includes attributes specific to a user, such as fullname, username, email, and password. This model also establishes a relationship with the Tale model.

Attributes:

fullname (String): The full name of the user. If not provided, it is auto-generated based on the user count.
username (String): The unique username of the user.
email (String): The unique email address of the user.
password (String): The hashed password of the user.
admin (Boolean): Indicates whether the user has admin privileges.
super_admin (Boolean): Indicates whether the user has super admin privileges.
about (String): A short bio or description of the user.
tales (Relationship): A one-to-many relationship with the Tale model, representing the tales created by the user.
Methods:

to_dict: Converts the user instance into a dictionary format, excluding sensitive data like password and super_admin status.
*Tale
The Tale model represents tales or stories created by users. It extends the BaseModel and includes attributes specific to a tale, such as title, content, and user_username.

Attributes:
title (String): The title of the tale.
content (String): The content or body of the tale.
user_username (String): A foreign key linking the tale to its creator (a user).

API Endpoints
The application provides RESTful API endpoints for interacting with User and Tale resources. Below are the main endpoints:

Tale Endpoints
GET /tales

Retrieves all tales.
Response: JSON array of all tales.
POST /tales

Creates a new tale.
Request Body: JSON object with title, content, and user_username.
Response: JSON object of the created tale.
GET /tales/<id>

Retrieves a specific tale by its ID.
Response: JSON object of the specified tale.
PUT /tales/<id>

Updates a specific tale by its ID.
Request Body: JSON object with the updated tale information.
Response: JSON object of the updated tale.
DELETE /tales/<id>

Deletes a specific tale by its ID.
Response: JSON object of the deleted tale.
User Endpoints
GET /users

Retrieves all users.
Response: JSON array of all users.
POST /users

Creates a new user.
Request Body: JSON object with username, email, password, and optionally fullname and about.
Response: JSON object of the created user.
GET /users/<username>

Retrieves a specific user by their username.
Response: JSON object of the specified user.
PUT /users/<username>

Updates a specific user by their username.
Request Body: JSON object with the updated user information.
Response: JSON object of the updated user.
GET /users/<username>/tales

Retrieves all tales created by a specific user.
Response: JSON array of tales created by the specified user.

Added a collections feeature for the users to connect related tales.