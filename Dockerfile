# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /loededogapi-docker

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

