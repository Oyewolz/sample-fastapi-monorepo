# FastAPI Monorepo - User & Notification Services

A simple FastAPI monorepo project demonstrating microservices architecture with user management and email notifications.

## 🏗️ Project Overview

This monorepo contains two microservices:

- **User Service**: Handles user registration, authentication, and management
- **Notification Service**: Sends email notifications (e.g., welcome emails with passwords)

### Features

- ✅ User registration with automatic email notification
- ✅ User login endpoint
- ✅ Shared library for common functionality (database, models, config)
- ✅ PostgreSQL database with SQLModel ORM
- ✅ Async database operations with asyncpg
- ✅ Docker support for consistent local development
- ✅ UV package manager for fast dependency management

## 📁 Project Structure

```
sample-fastapi-monorepo/
├── services/
│   ├── user-service/          # User management service
│   │   ├── src/
│   │   │   └── user_service/
│   │   └── pyproject.toml
│   └── notification-service/  # Email notification service
│       ├── src/
│       │   └── notification_service/
│       └── pyproject.toml
├── libs/
│   └── shared-lib/            # Shared library (database, models, config)
│       ├── src/
│       │   └── shared_lib/
│       │       ├── config/
│       │       ├── database/
│       │       └── models/
│       └── pyproject.toml
├── docker-compose.local.yml   # Local development setup
├── docker-compose.database.yml # Database only
├── Dockerfile.user-service
├── Dockerfile.notification-service
├── pyproject.toml             # Root workspace config
├── uv.lock                    # Dependency lock file
└── .env                       # Environment variables
```

## 🚀 Getting Started

### Prerequisites

- **Docker & Docker Compose** (Recommended for local development)
- **Python 3.12+** (if running without Docker)
- **UV package manager** (if running without Docker)

### Installation

#### Option 1: Using Docker (Recommended)

Running with Docker ensures consistency across different development environments and avoids setup differences.

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sample-fastapi-monorepo
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start all services with Docker Compose**
   ```bash
   docker-compose -f docker-compose.local.yml up --build
   ```

   This will start:
   - PostgreSQL database (port 5432)
   - User Service (port 8000)
   - Notification Service (port 8001)

#### Option 2: Local Development (Without Docker)

1. **Install UV package manager**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # or
   pip install uv
   ```

2. **Clone and setup**
   ```bash
   git clone <repository-url>
   cd sample-fastapi-monorepo
   ```

3. **Create environment file**
   ```bash
   cat > .env << EOF
   DATABASE_URL=postgresql+asyncpg://fast-api:test1234@localhost:5432/fast-api
   DEBUG=True
   APP_HOST=0.0.0.0
   APP_PORT=8000
   EOF
   ```

4. **Start PostgreSQL database**
   ```bash
   docker-compose -f docker-compose.database.yml up -d
   ```

5. **Sync dependencies**
   ```bash
   uv sync
   ```

6. **Run services**

   Terminal 1 - User Service:
   ```bash
   cd services/user-service
   uv run uvicorn user_service:app --reload --port 8000
   ```

   Terminal 2 - Notification Service:
   ```bash
   cd services/notification-service
   uv run uvicorn notification_service:app --reload --port 8001
   ```

## 📚 UV Package Manager - Daily Commands

### Workspace Management

```bash
# Sync all workspace dependencies
uv sync

# Sync with frozen lock file (production)
uv sync --frozen

# Update all dependencies
uv sync --upgrade
```

### Creating New Services

```bash
# Create a new service
mkdir -p services/new-service/src/new_service
cd services/new-service

# Initialize the service
uv init --lib

# Edit pyproject.toml to add dependencies
uv add fastapi uvicorn

# Add shared library dependency
# In pyproject.toml, add:
# [tool.uv.sources]
# shared-lib = { workspace = true }

# Register in root pyproject.toml workspace members:
# members = ["services/new-service", ...]
```

### Creating New Shared Libraries

```bash
# Create a new shared library
mkdir -p libs/new-lib/src/new_lib
cd libs/new-lib

# Initialize the library
uv init --lib

# Add dependencies
uv add sqlalchemy pydantic

# Register in root pyproject.toml workspace members:
# members = ["libs/new-lib", ...]
```

### Dependency Management

```bash
# Add a dependency to current package
uv add package-name

# Add a dev dependency
uv add --dev pytest

# Add a specific version
uv add "fastapi>=0.100.0"

# Remove a dependency
uv remove package-name

# Show installed packages
uv pip list

# Show dependency tree
uv tree
```

### Running Commands

```bash
# Run a Python script
uv run python script.py

# Run a module
uv run python -m module_name

# Run with environment variables
uv run --env-file .env python script.py

# Run tests
uv run pytest

# Run a specific service
cd services/user-service
uv run uvicorn user_service:app --reload
```

### Lock File Management

```bash
# Update lock file
uv lock

# Update specific package
uv lock --upgrade-package package-name

# Verify lock file is up to date
uv lock --check
```

## 🔧 Environment Variables

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=postgresql+asyncpg://fast-api:test1234@localhost:5432/fast-api

# Application
DEBUG=True
APP_HOST=0.0.0.0
APP_PORT=8000

# Email (for notification service)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## 🎯 API Endpoints

### User Service (Port 8000)

#### Register User
```bash
POST /users/register
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

**Response**: User created + notification email sent with password

#### Login
```bash
POST /users/login
Content-Type: application/json

{
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

**Response**: Authentication token

#### Get User
```bash
GET /users/{user_id}
Authorization: Bearer <token>
```

### Notification Service (Port 8001)

#### Send Email
```bash
POST /notifications/send
Content-Type: application/json

{
  "to": "user@example.com",
  "subject": "Welcome!",
  "body": "Your password is: ..."
}
```

## 🗄️ Database

### Database Schema

The project uses PostgreSQL with the following tables:

**ftuser** (User table)
- `id` (Primary Key)
- `first_name`
- `last_name`
- `email`
- `password` (hashed)
- `created_at`
- `updated_at`
- `deleted`
- `active`

**role** (Role table)
- `id` (Primary Key)
- `name`
- `description`
- `created_at`
- `updated_at`
- `deleted`
- `active`

### Database Migrations

Tables are automatically created on application startup using SQLModel's `create_all()` method.

### Accessing the Database

```bash
# Using Docker
docker exec -it fast_api_db psql -U fast-api -d fast-api

# List tables
\dt

# Query users
SELECT * FROM ftuser;

# Exit
\q
```

## 🧪 Testing

### Run Tests

```bash
# Run all tests
uv run pytest

# Run tests for specific service
cd services/user-service
uv run pytest

# Run with coverage
uv run pytest --cov=user_service --cov-report=html
```

### Manual Testing with cURL

```bash
# Register a user
curl -X POST http://localhost:8000/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane@example.com",
    "password": "myPassword123"
  }'

# Login
curl -X POST http://localhost:8000/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "jane@example.com",
    "password": "myPassword123"
  }'
```

## 🐳 Docker Commands

### Development

```bash
# Start all services
docker-compose -f docker-compose.local.yml up

# Start in detached mode
docker-compose -f docker-compose.local.yml up -d

# Rebuild and start
docker-compose -f docker-compose.local.yml up --build

# Stop all services
docker-compose -f docker-compose.local.yml down

# Stop and remove volumes
docker-compose -f docker-compose.local.yml down -v
```

### Database Only

```bash
# Start only PostgreSQL
docker-compose -f docker-compose.database.yml up -d

# Stop database
docker-compose -f docker-compose.database.yml down

# View database logs
docker logs fast_api_db

# Access database shell
docker exec -it fast_api_db psql -U fast-api -d fast-api
```

### Docker Utilities

```bash
# View running containers
docker ps

# View logs for a service
docker-compose -f docker-compose.local.yml logs user-service
docker-compose -f docker-compose.local.yml logs -f user-service  # Follow logs

# Restart a service
docker-compose -f docker-compose.local.yml restart user-service

# Execute command in container
docker-compose -f docker-compose.local.yml exec user-service bash

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune
```

## 🔍 Troubleshooting

### Common Issues

**Issue**: `ImportError: cannot import name 'UTC' from 'sqlmodel'`
- **Solution**: UTC should be imported from `datetime`, not `sqlmodel`

**Issue**: `ValueError: the greenlet library is required`
- **Solution**: Add `greenlet>=3.2.4` to shared-lib dependencies
  ```bash
  cd libs/shared-lib
  uv add greenlet
  ```

**Issue**: Tables not created automatically
- **Solution**: Ensure models are imported before `SQLModel.metadata.create_all()` is called
  ```python
  from shared_lib.database.models import FTUser, Role  # Import models
  ```

**Issue**: Environment variables not loading
- **Solution**: Check `.env` file location (should be at repository root) and verify `pydantic-settings` is installed

**Issue**: Database connection refused
- **Solution**: Ensure PostgreSQL is running
  ```bash
  docker-compose -f docker-compose.database.yml up -d
  ```

### Debugging

```bash
# Check if services are running
docker ps

# View service logs
docker-compose -f docker-compose.local.yml logs

# Check database connection
docker exec -it fast_api_db pg_isready -U fast-api

# Verify environment variables are loaded
cd services/user-service
uv run python -c "from user_service.config import get_config; print(get_config().DATABASE_URL)"
```

## 📝 Development Workflow

### Adding a New Feature

1. **Create a new branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make changes to the code**

3. **Add dependencies if needed**
   ```bash
   cd services/user-service
   uv add new-package
   ```

4. **Sync workspace**
   ```bash
   cd ../..
   uv sync
   ```

5. **Test locally**
   ```bash
   docker-compose -f docker-compose.local.yml up --build
   ```

6. **Commit and push**
   ```bash
   git add .
   git commit -m "Add new feature"
   git push origin feature/new-feature
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- **oyewolz** - [oyewoletaiwo219@gmail.com](mailto:oyewoletaiwo219@gmail.com)

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- SQLModel for the elegant ORM
- UV for blazing fast package management
- PostgreSQL for reliable data storage