docker-compose build
docker-compose up -d
docker-compose run delivery_hero python manage.py migrate
docker-compose run delivery_hero python manage.py loaddata fixtures/init.json
docker-compose restart

