setup:
	docker-compose build
	docker-compose up -d
	docker-compose run django python manage.py migrate
	docker-compose run django python manage.py loaddata fixtures/initial_data.json
	docker-compose restart
run:
	docker-compose up -d
restart:
	docker-compose restart
stop:
	docker-compose stop
test:
	#docker-compose run django pytest
	docker-compose run django python manage.py test
eslint:
	./node_modules/.bin/eslint --env browser "assets/js/**"
dump_fixture:
	docker-compose run django python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 --format=json > fixtures/initial_data.json
manage:
	docker-compose run django python manage.py ${args}
cmd:
	docker-compose run django ${args}
