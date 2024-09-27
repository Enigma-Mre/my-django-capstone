# my-django-capstone

# Index

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
   - [Using `.venv`](#using-venv)
   - [Using Docker](#using-docker)
4. [Important Notes](#important-notes)
5. [Installation](#installation)

## Overview

This is a Django project that allows users to [briefly describe the functionality of your application].
This README outlines the steps to build and run the application both using a virtual environment (`.venv`) and Docker.

## Prerequisites

- Python 3.10 or later
- Docker and Docker Compose (if using Docker)
- Git

## Setup Instructions

### Using `.venv`

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Enigma-Mre/my-django-capstone.git
   cd my-django-capstone

## Create and Activate a Virtual Environment:

- python -m venv .venv
- source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

## Install Dependencies:

- pip install -r requirements.txt

## Set Environment Variables:

- SECRET_KEY='your_secret_key'
- DEBUG=True  # Change to False in production
- DATABASE_URL='your_database_url'  # Example: postgres://user:password@localhost:5432/dbname

## Run Migrations:

- python manage.py migrate

## Run the Development Server:

- python manage.py runserver
- The application should now be running at http://127.0.0.1:8000

### Using Docker:

1. Clone the Repository: If you haven't already done so, follow the same steps as in the .venv setup to clone your repository.
2. Build the Docker Image:
- docker build -t my-django-app .
  
3. Run the Docker Container:
- docker run -p 8000:8000 my-django-app
- The application should now be accessible at http://127.0.0.1:8000.

### Important Notes

    Secrets Management: Do not commit sensitive information such as passwords or access tokens to public repositories. Always use environment variables or a .env file to manage secrets.
    Database Configuration: Ensure that you have your database configured and accessible before running the application. Update your .env file with the appropriate credentials.

## Installation

Follow these steps to install the project dependencies:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Enigma-Mre/my-django-capstone.git
   cd my-django-capstone
