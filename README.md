# Django REST API Template (t8787)

A production-ready Django REST API template with modern tooling and comprehensive features for building scalable web applications.

## 🚀 Features

### Core Framework
- **Django 5.2.1** - Latest Django framework with async support
- **Django REST Framework** - Powerful API development toolkit
- **ASGI/WSGI Support** - Both async (Uvicorn) and sync (Gunicorn) server support
- **Channels** - WebSocket and async support

### Authentication & Authorization
- **Djoser** - Complete authentication system with token-based auth
- **Token Authentication** - Secure API access with DRF tokens
- **User Management** - Registration, login, password reset endpoints

### Database & Caching
- **PostgreSQL** - Primary database with connection pooling
- **Redis** - Caching and session storage
- **Django Cachalot** - Automatic ORM query caching
- **Database URL Configuration** - Easy database setup via environment variables

### Task Processing
- **Django Tasks Scheduler** - Background task processing with Redis
- **Worker Support** - Dedicated worker processes for async tasks
- **Queue Management** - Configurable task queues

### Storage & Media
- **Django Storages** - S3-compatible storage backend
- **Cloudflare R2 Support** - Cost-effective S3-compatible storage
- **Static File Management** - Automated static file collection and serving

### API Documentation
- **DRF Spectacular** - OpenAPI 3.0 schema generation
- **Swagger UI** - Interactive API documentation at `/docs/`
- **API Versioning** - Namespace-based API versioning

### Development & Monitoring
- **Django Extensions** - Enhanced development tools
- **Django GUID** - Request correlation IDs for better logging
- **Sentry Integration** - Error tracking and performance monitoring
- **CORS Support** - Cross-origin resource sharing configuration
- **Comprehensive Logging** - Structured logging with correlation IDs

### Configuration Management
- **Django Constance** - Dynamic configuration with Redis backend
- **Environment Variables** - 12-factor app configuration
- **Python Dotenv** - Local development environment support

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.13+
- PostgreSQL
- Redis
- UV package manager (recommended) or pip

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd t8787
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Using UV (recommended)
   uv sync

   # Or using pip
   pip install -e .
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```env
   # Required Environment Variables
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
   REDIS_URL=redis://localhost:6379/0
   
   # Storage Configuration (R2/S3)
   R2_BUCKET_NAME=your-bucket-name
   R2_KEY=your-access-key
   R2_SECRET=your-secret-key
   R2_DOMAIN_NAME=your-domain.com
   R2_ENDPOINT_URL=https://your-account-id.r2.cloudflarestorage.com
   R2_URL_PROTOCOL=https:
   
   # Optional Configuration
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   SENTRY_DSN=your-sentry-dsn-here
   ```

5. **Run database migrations**
   ```bash
   cd foobar
   uv run python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   uv run python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   uv run python manage.py collectstatic --noinput
   ```

8. **Start the development server**
   ```bash
   ./start.sh
   ```

   Or manually:
   ```bash
   uv run python -m uvicorn foobar.asgi:application --reload --host 0.0.0.0 --port 8888
   ```

9. **Start the worker process** (in a separate terminal)
   ```bash
   cd foobar
   uv run python manage.py scheduler_worker default
   ```

### Using Docker Compose (Development)

```bash
docker-compose up --build
```

This will start:
- Web application on `http://localhost:8110`
- PostgreSQL database
- Redis cache
- MinIO (S3-compatible storage)
- Background worker

## 🧪 Testing

Run the test suite:
```bash
cd foobar
uv run python manage.py test
```

## 📚 API Documentation

Once the server is running, you can access:
- **Swagger UI**: `http://localhost:8888/docs/`
- **OpenAPI Schema**: `http://localhost:8888/schema/`
- **Admin Interface**: `http://localhost:8888/admin/`

## 🚀 Production Deployment

### Required Environment Variables for Production

```env
# Core Configuration
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/database
REDIS_URL=redis://host:port/db

# Domain Configuration
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://app.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://app.yourdomain.com

# Storage Configuration (Cloudflare R2 or AWS S3)
R2_BUCKET_NAME=your-production-bucket
R2_KEY=your-access-key-id
R2_SECRET=your-secret-access-key
R2_DOMAIN_NAME=your-custom-domain.com
R2_ENDPOINT_URL=https://account-id.r2.cloudflarestorage.com
R2_URL_PROTOCOL=https:

# Monitoring (Optional but recommended)
SENTRY_DSN=https://your-sentry-dsn@sentry.io/project-id
```

### Deployment Steps

1. **Set up your infrastructure**
   - PostgreSQL database
   - Redis instance
   - S3-compatible storage (Cloudflare R2 recommended)

2. **Configure environment variables**
   Set all the required environment variables listed above in your deployment platform.

3. **Deploy the application**
   ```bash
   # Install dependencies
   uv sync --frozen

   # Run migrations
   cd foobar && uv run python manage.py migrate

   # Collect static files
   uv run python manage.py collectstatic --noinput

   # Start the application
   uv run gunicorn foobar.asgi:application -k uvicorn_worker.UvicornWorker --bind 0.0.0.0:8000
   ```

4. **Start worker processes**
   ```bash
   cd foobar && uv run python manage.py scheduler_worker default
   ```

### Recommended Production Setup

- **Web Server**: Nginx as reverse proxy
- **Application Server**: Gunicorn with Uvicorn workers
- **Database**: PostgreSQL with connection pooling
- **Cache**: Redis cluster
- **Storage**: Cloudflare R2 or AWS S3
- **Monitoring**: Sentry for error tracking
- **Process Management**: Supervisor or systemd

## 🔧 Customization

This is a template project. To customize it for your needs:

1. **Rename the project**
   - Find and replace `foobar` throughout the project with your project name
   - Rename the `foobar` directory to your project name
   - Update `pyproject.toml` with your project details

2. **Add your models**
   - Create models in `foobar/api/models.py`
   - Create serializers and views
   - Add URL patterns

3. **Configure your specific requirements**
   - Update dependencies in `pyproject.toml`
   - Modify settings as needed
   - Add custom middleware or authentication

## 📝 License

This project is a template and can be used freely for your projects.

## 🤝 Contributing

This is a template project. Feel free to fork and modify for your needs.

