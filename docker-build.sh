docker-compose build
docker-compose up -d
docker-compose run test_api_django python manage.py migrate
docker-compose run test_api_django python manage.py loaddata fixtures/init.json
docker-compose restart

