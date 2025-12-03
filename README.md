# Test API Django

A Django REST API project with PostgreSQL database support.

## Features

- Django 4.2 (LTS)
- Django REST Framework
- PostgreSQL database
- Docker and Docker Compose setup
- Pytest for testing
- Environment-based configuration

## Prerequisites

- Docker
- Docker Compose
- Make (optional, for convenience commands)

## Environment Variables

Copy the example environment file and customize it:

```bash
cp .env.example .env
```

Required environment variables:
- `SECRET_KEY`: Django secret key (generate a secure one for production)
- `DEBUG`: Set to `true` for development, `false` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_*`: Database configuration variables

## Setup and Installation

### Using Make (Recommended)

```bash
# Build and start the project
make setup

# Run the development server
make run

# Run tests
make test

# Stop the services
make stop

# Restart services
make restart
```

### Manual Docker Commands

```bash
# Build containers
docker-compose build

# Start services
docker-compose up -d

# Run migrations
docker-compose run django python manage.py migrate

# Load initial data (if available)
docker-compose run django python manage.py loaddata fixtures/init.json

# Create a superuser
docker-compose run django python manage.py createsuperuser

# Run tests
docker-compose run django pytest
```

## Development

### Running Management Commands

```bash
# Using Make
make manage args="<command>"

# Example: Create a superuser
make manage args="createsuperuser"

# Direct docker-compose
docker-compose run django python manage.py <command>
```

### Running Custom Commands

```bash
# Using Make
make cmd args="<command>"

# Direct docker-compose
docker-compose run django <command>
```

### Creating Fixtures

```bash
make dump_fixture
```

## Testing

Run the test suite:

```bash
make test
```

Or with docker-compose directly:

```bash
docker-compose run django pytest
```

## Admin Access

Default credentials (after running `make setup` with initial fixtures):
- Username: `admin`
- Password: `123`

**⚠️ Change these credentials in production!**

## Project Structure

```
.
├── docker_files/          # Docker configuration files
├── fixtures/              # Database fixtures
├── project/              # Main Django project
│   ├── apps/            # Django applications
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL configuration
│   └── tests.py         # Basic tests
├── static_files/         # Static files
├── docker-compose.yaml   # Docker Compose configuration
├── Makefile             # Convenience commands
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Security Notes

1. **Never commit `.env` files** - they contain sensitive information
2. **Change the SECRET_KEY** in production to a strong, unique value
3. **Set DEBUG=false** in production
4. **Configure ALLOWED_HOSTS** properly for your domain
5. **Change default admin credentials** immediately after setup
6. **Use strong passwords** for database and admin accounts

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## License

[Add your license information here]
