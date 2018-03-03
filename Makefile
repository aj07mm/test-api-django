setup:
	docker-compose build
	docker-compose up -d
	docker-compose run test_api_django python manage.py migrate
	docker-compose run test_api_django python manage.py loaddata fixtures/init.json
	docker-compose restart
run:
	docker-compose up -d
restart:
	docker-compose restart
stop:
	docker-compose stop
test:
	docker-compose run test_api_django python manage.py test
manage:
	docker-compose run test_api_django python manage.py ${args}
cmd:
	docker-compose run test_api_django ${args}
