# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
# (you may not have any in this case)
RUN pip install -r requirements.txt

# Define the command to run your script
CMD ["python", "./Noasync.py"]