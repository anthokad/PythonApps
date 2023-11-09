# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your app will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "myapp.py"]
