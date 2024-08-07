# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PIPENV_VENV_IN_PROJECT=1

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install dependencies
RUN pipenv sync

# Copy the rest of the application code
COPY . /app

# Run Alembic migrations and seed script
CMD ["sh", "-c", "pipenv run alembic upgrade head && pipenv run python seed.py"]