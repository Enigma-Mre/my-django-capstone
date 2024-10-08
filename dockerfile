# Use the official Python image from the Docker Hub
<<<<<<< HEAD
=======
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Run migrations (optional, depending on your setup)
# CMD ["python", "manage.py", "migrate"]

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use the official Python image from the Docker Hub
>>>>>>> docs
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run migrations and start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
