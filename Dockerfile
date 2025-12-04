# Use the official Python image from the Docker Hub
FROM python:3.9-slim

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt