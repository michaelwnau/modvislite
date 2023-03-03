# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . .

# Expose port 8000
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=project_modvislite.settings
ENV PYTHONUNBUFFERED=1

# Run the Django app using Gunicorn
CMD gunicorn project_modvislite.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4
