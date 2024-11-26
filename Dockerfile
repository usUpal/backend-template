FROM python:3.9.6-slim-buster as dev

# Install dependencies
RUN apt-get update -y && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app/src

# Export requirements from poetry
COPY pyproject.toml poetry.lock ./
RUN pip install poetry==1.4.2 \
    && poetry config virtualenvs.create false \
    && poetry export -f requirements.txt --output requirements.txt \
    && pip install -r requirements.txt

# Copy the actual application
COPY . .

# Remove build dependencies
RUN apt-get purge -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Command to run the application
CMD ["uvicorn", "--host", "0.0.0.0", "app.main:app", "--reload"]