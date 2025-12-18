# Pytest API Framework

A comprehensive testing framework built with Python and Pytest for API testing and database operations using PostgreSQL.

## 📋 Project Overview

This project provides a robust framework for testing REST APIs and PostgreSQL database operations. It combines API client utilities with database connection management, following Python best practices and Pytest conventions.

### Key Features

- **API Testing**: Client abstraction for REST API endpoints (GET, POST, PUT, DELETE)
- **Database Operations**: Connection pooling and utility methods for PostgreSQL interactions
- **Test Fixtures**: Reusable Pytest fixtures for API client and database connections
- **Type Hints**: Full type annotations for better IDE support and code clarity
- **Docker Support**: Pre-configured PostgreSQL container with initialization scripts
- **Error Handling**: Comprehensive error handling and logging throughout the framework

## 🏗️ Architecture

### Project Structure

```
pytest-api-framework/
├── api-framework/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── api_client.py         # REST API client abstraction
│   │   ├── api_endpoints.py      # API endpoint definitions
│   │   └── database.py           # PostgreSQL connection management
│   ├── tests/
│   │   ├── conftest.py           # Pytest fixtures and configuration
│   │   ├── test_db_connection.py # Database tests
│   │   ├── test_activities.py    # API endpoint tests
│   │   └── data/
│   │       └── activities.py     # Test data definitions
│   ├── reports/                  # Generated test reports
│   ├── requirements.txt          # Python dependencies
│   └── pytest.ini               # Pytest configuration
├── docker/
│   ├── docker-compose.yml       # PostgreSQL container setup
│   └── init.sql                 # Database initialization script
└── README.md
```

### Core Components

#### 1. **API Client** (`src/api_client.py`)
Provides a simple abstraction for HTTP operations:
- `APIClient.get()` - Retrieve data
- `APIClient.post()` - Create resources
- `APIClient.put()` - Update resources
- `APIClient.delete()` - Remove resources

Supports URL path parameters and query strings.

#### 2. **Database Connection** (`src/database.py`)
Manages PostgreSQL connections with connection pooling:
- `execute_query()` - Fetch multiple rows as tuples
- `execute_query_one()` - Fetch a single row
- `execute_query_dict()` - Fetch rows as dictionaries
- `execute_update()` - Insert, update, or delete operations
- `execute_many()` - Batch operations
- Context manager support for safe connection handling

Features:
- Connection pooling (SimpleConnectionPool)
- Automatic commit/rollback
- SQL injection prevention via parameterized queries
- Type hints and comprehensive docstrings

#### 3. **Pytest Fixtures** (`tests/conftest.py`)
Reusable test fixtures:
- `api_client` - Pre-configured REST API client (module scope)
- `db_connection` - PostgreSQL connection instance (module scope)

## 🐳 Docker Setup for Database Testing

### Prerequisites
- Docker and Docker Compose installed
- No need to install PostgreSQL locally

### Quick Start

1. **Start the PostgreSQL Container**

```bash
cd docker
docker-compose up -d
```

This will:
- Create a PostgreSQL container with credentials:
  - **User**: `user`
  - **Password**: `1234`
  - **Database**: `testdb`
  - **Port**: `5432`
- Initialize the database with sample data from `init.sql`

2. **Verify the Container is Running**

```bash
docker-compose ps
```

3. **Access the Database** (optional)

```bash
docker-compose exec db psql -U user -d testdb
```

### Database Schema

The initialization script (`docker/init.sql`) creates the following table:

```sql
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(100),
    age INT
);
```

**Sample Data**:
```
id | fname   | age
---|---------|-----
1  | Alice   | 30
2  | Bob     | 25
3  | Charlie | 35
```

### Environment Configuration

Update `tests/conftest.py` with your PostgreSQL credentials:

```python
@pytest.fixture(scope="module")
def db_connection():
    db = DatabaseConnection(
        host="localhost",        # Change if Docker is on different host
        database="testdb",       # Match POSTGRES_DB from docker-compose.yml
        user="user",            # Match POSTGRES_USER from docker-compose.yml
        password="1234",        # Match POSTGRES_PASSWORD from docker-compose.yml
        port=5432
    )
    yield db
    db.close()
```

### Stop and Clean Up

```bash
# Stop the container
docker-compose down

# Remove the container and volumes
docker-compose down -v
```

## 🚀 Installation & Execution

### 1. Install Dependencies

```bash
### Cloning the repository
git clone https://github.com/AlexAlexandreAlves/pytest-api-framework.git

### Run through the venv (virtual environment), for this, you need to create and activate it first
python3 -m venv {$name}
source {$name}/bin/activate 

### Copy all folders and files in the main project and past into your recent created env-folder, and then install the dependencies:
cd {your-venv-folder}
pip install -r requirements.txt

```

**Key Dependencies**:
- `pytest` - Testing framework
- `requests` - HTTP client library
- `psycopg2-binary` - PostgreSQL adapter for Python
- `mypy` - Static type checker
- `pytest-reporter-html1` - HTML test report generation

### 2. Run Tests

```bash
# Run all tests
pytest

# Run tests with @pytest.mark (example: testdb)
pytest -m testdb

# Run with verbose output
pytest -v

# Run with print statements visible
pytest -s -v

# Run specific test file
pytest tests/test_db_connection.py

# Generate HTML report
pytest --html=reports/html1-report.html
```

### 3. Running Database Tests

Ensure the Docker container is running before executing database tests:

```bash
# Start PostgreSQL
cd docker && docker-compose up -d && cd ..

# Run database tests
pytest tests/test_db_connection.py -v
```

## 📝 Example Test Usage

### Testing the Database Connection

```python
def test_users(db_connection):
    # Query the database
    people = db_connection.execute_query_dict(
        "SELECT * FROM people WHERE id = %s",
        (1,)
    )
    
    # Validate results
    assert len(people) > 0
    person = people[0]
    assert person["fname"] == "Alice"
    assert person["age"] == 30
```

### Testing API Endpoints

```python
def test_get_activity(api_client):
    response = api_client.get(Endpoints.ACTIVITIES_BY_ID, id=1)
    assert response.status_code == 200
```

## 🔒 Best Practices

- **Parameterized Queries**: Always use `%s` placeholders to prevent SQL injection
- **Connection Management**: Use context managers (`with` statements) for safe connection handling
- **Fixtures**: Leverage Pytest fixtures for setup and teardown
- **Type Hints**: Use type annotations for better code documentation
- **Error Handling**: Catch and log errors appropriately
- **Test Isolation**: Each test should be independent and repeatable
- **Async Support**: For I/O-bound tests, consider using `pytest-asyncio`

## 📚 Dependencies

See `requirements.txt` for the complete list. Key dependencies:

| Package | Version | Purpose |
|---------|---------|---------|
| pytest | Latest | Testing framework |
| requests | Latest | HTTP client |
| psycopg2-binary | Latest | PostgreSQL adapter |
| mypy | Latest | Type checking |
| pytest-reporter-html1 | Latest | HTML reports |

## 🛠️ Troubleshooting

### PostgreSQL Connection Issues
- Verify Docker container is running: `docker-compose ps`
- Check credentials in `conftest.py` match `docker-compose.yml`
- Ensure port 5432 is not in use: `lsof -i :5432`

### Import Errors
- Activate virtual environment: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### Test Failures
- Use `-v` flag for verbose output
- Use `-s` flag to see print statements
- Check database initialization: `docker-compose logs db`

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

AlexAlexandreAlves

---

**Happy Testing! 🧪**