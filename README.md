# Django Movie API Project

This Django project provides an API to Register/Login User to get the Token required for authentication, Get Hello, Django! message, Process a video using OpenCV & manage a collection of movies.

## Setup Instructions

### Clone the Project

    git clone https://github.com/shaikhsaalem1997/bia-assignment.git

    cd bia-assignment

### Installation

Create and activate a virtual environment (recommended).
Install project dependencies from requirements.txt.

    pip install -r requirements.txt

### Running the Project

    python manage.py makemigrations

    python manage.py migrate

    python manage.py runserver

The server will start at http://localhost:8000/


## API Endpoints

### Hello Django Message

* Endpoint: http://localhost:8000/hello/
* Method: GET
* Header: Content-Type: application/json
* Description: Retrieves a "Hello, Django!" message.

### Processing Video

* Endpoint: http://localhost:8000/process-video/
* Method: GET
* Header: Content-Type: application/json
* Description: Dwonload and save the custom made video with OpenCV.
* Message: Video generation successful at "Root_project_directory + static\\processed_videos\\generated_video.mp4".

## User Registration and Authentication

To interact with authenticated endpoints, register a user and obtain token.

### User Registration:

* Endpoint: http://localhost:8000/signup/
* Method: POST
* Header: Content-Type: application/json
* Request Body: Include username, password, and email.
* Description: Registers a new user. Obtain the token.

### User Login:

* Endpoint: http://localhost:8000/login/
* Method: POST
* Header: Content-Type: application/json
* Request Body: Include username and password.
* Description: Obtain access tokens.

## Movie Management

### Get All Movies:

* Endpoint: http://localhost:8000/movies/
* Method: GET
* Header: { Content-Type: application/json, Authorization: Token <your_token_here> }
* Description: Retrieves a list of all movies.

### Add New Movie:

* Endpoint: http://localhost:8000/movies/
* Method: POST
* Header: { Content-Type: application/json, Authorization: Token <your_token_here> }
* Request Body: Include title & description(optional)
* Description: Adds a new movie to the collection.
