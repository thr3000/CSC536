# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV STATIC_ROOT /usr/src/app/staticfiles

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Specify the command to run on container start
CMD ["gunicorn", "csc536Django.wsgi:application", "--bind", "0.0.0.0:8000"]

# Expose the port the app runs on
EXPOSE 8000