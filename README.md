

# Kiko Network API for Data Fetching 

## Overview

This project is a FastAPI-based web application that provides APIs for user authentication and air quality data management. It is designed with scalability in mind and structured for easy maintainability.

## Features

- **User Authentication**: Implements secure login and registration features.
- **Air Quality Data**: API endpoints to retrieve and store air quality data.
- **Database Integration**: Uses SQLAlchemy ORM to interact with a PostgreSQL database.
- **Environment Configuration**: Uses `.env` for environment variable management.
- **Docker Support**: Comes with Docker setup for easy containerization and deployment.

## Directory Structure

```
.
├── app
│   ├── air_quality
│   │   ├── air_quality.py
│   │   └── __init__.py
│   ├── auth
│   │   ├── auth.py
│   │   └── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── database
│   │   ├── database.py
│   │   └── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   └── schemas
│       ├── __init__.py
│       └── schemas.py
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── run.sh
```

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add the following variables:
   ```
   DATABASE_URL=<your_database_url>
   SECRET_KEY=<your_secret_key>
   ```

6. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Running with Docker

To run the project with Docker:

1. **Build the Docker image**:
   ```bash
   docker build -t project-name .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 8000:8000 project-name
   ```
