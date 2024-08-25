Overview
This project is a simple Flask-based 3-tier web application, designed to run across three Docker containers:

Nginx: Acts as a reverse proxy and listens on port 80.
MySQL: Serves as the database and listens on port 3306.
App: The Flask application, which interacts with both Nginx and MySQL.
Network Configuration
Nginx Container: Connected to the frontend Docker network.
MySQL Container: Connected to the backend Docker network.
App Container: Connected to both frontend and backend Docker networks. It acts as the intermediary between Nginx and MySQL, ensuring that the database remains isolated from direct user access.
Setup and Usage
1.Build and Run Containers
After setting up the project, execute the abrakadabra.sh script to build and run all the necessary containers.
./abrakadabra.sh
2.Access the Application
Open your web browser and navigate to:
http://localhost:80
This will display the welcome page of the application.

3.Available Routes:
/all: Displays all names stored in the database.
/add: Allows you to add a new person to the database.
/find: Enables you to search for a specific person in the database.
/delete: Provides functionality to delete a specific person from the database.

Notes:
Network Separation: The Nginx and MySQL containers are on separate networks (frontend and backend, respectively) to ensure that the database is not directly accessible by end users.
Security: This architecture maintains separation between web and database services, enhancing security by limiting direct database access.
