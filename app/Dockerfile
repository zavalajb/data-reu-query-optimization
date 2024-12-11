# Use the official Python image as the base image
#
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY . /app/app
#COPY queries /app/queries
#COPY README.md /app/

# Set the environment variable for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]