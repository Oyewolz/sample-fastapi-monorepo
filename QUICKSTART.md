# Quick Start Guide

Get up and running with the FastAPI Monorepo in 5 minutes!

## 🚀 Fastest Way to Start (Docker)

**Recommended**: Use Docker to avoid environment setup differences.

```bash
# 1. Clone the repository
git clone <repository-url>
cd sample-fastapi-monorepo

# 2. Create environment file
cp .env.example .env

# 3. Start everything with Docker
docker-compose -f docker-compose.local.yml up --build
```

That's it! Your services are now running:
- **User Service**: http://localhost:8000
- **Notification Service**: http://localhost:8001
- **PostgreSQL**: localhost:5432

## 📝 Test the API

### 1. Register a User

```bash
curl -X POST http://localhost:8000/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "myPassword123"
  }'
```

**What happens:**
- User is created in the database
- Notification service sends a welcome email with the password

### 2. Login

```bash
curl -X POST http://localhost:8000/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "myPassword123"
  }'
```

### 3. View API Documentation

Open your browser:
- User Service Docs: http://localhost:8000/docs
- Notification Service Docs: http://localhost:8001/docs

## 🛠️ Local Development (Without Docker)

If you prefer to run services locally:

```bash
# 1. Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Start database only
docker-compose -f docker-compose.database.yml up -d

# 3. Sync dependencies
uv sync

# 4. Run user service
cd services/user-service
uv run uvicorn user_service:app --reload --port 8000

# 5. In another terminal, run notification service
cd services/notification-service
uv run uvicorn notification_service:app --reload --port 8001
```

## 🔍 Verify Everything Works

```bash
# Check if database is running
docker ps | grep fast_api_db

# Check if services are responding
curl http://localhost:8000/docs
curl http://localhost:8001/docs

# Access database
docker exec -it fast_api_db psql -U fast-api -d fast-api
# Then run: \dt to see tables
```

## 🎯 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the API at http://localhost:8000/docs
- Check the database schema
- Add your own endpoints

## 🐛 Troubleshooting

**Port already in use?**
```bash
# Change ports in docker-compose.local.yml or .env
```

**Database connection error?**
```bash
# Restart database
docker-compose -f docker-compose.database.yml restart
```

**Need to reset everything?**
```bash
# Stop and remove all containers and volumes
docker-compose -f docker-compose.local.yml down -v
# Start fresh
docker-compose -f docker-compose.local.yml up --build
```

## 📚 Learn More

- [Full Documentation](README.md)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)

