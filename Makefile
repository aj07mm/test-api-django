setup:
	docker-compose build
	docker-compose up -d
	docker-compose run python manage.py migrate
	docker-compose run python manage.py loaddata fixtures/init.json
	docker-compose restart
	docker container prune
run:
	docker-compose up -d
restart:
	docker-compose restart
stop:
	docker-compose stop
test:
	docker-compose run python manage.py test

