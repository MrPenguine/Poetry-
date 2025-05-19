FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy the action code
COPY . /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Set the entrypoint
ENTRYPOINT ["python", "-m", "diff_poetry_lock.run_poetry"]
