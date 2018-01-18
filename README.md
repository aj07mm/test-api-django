# Delivery Hero backend test

How to run:

```
docker-compose up -d
docker-compose run delivery_hero python manage.py migrate
docker-compose run delivery_hero python manage.py loaddata init.json
```

login:

	username: admin
	password: 123

---

Requirements:


The objective of this code challenge is to develop a backend service or api.

The api responses will use json over http

We would like to have a CRUD (create, read, update, delete) on restaurant objects. A restaurant object will have the following fields:
- id: int
- name: string
- opens_at: datetime
- closes_at: datetime

For example, a call to the system could be something like:

GET /restaurant/1

And the output would be

{
 "id": 1,
 "name": "Pizza Berlin",
  ...

}

The stack to use is python3 and a python web framework of your choice (flask or django would be perfect, but it is up to you)
Make the decisions and asumptions you need or want.
The deliverable will be a public git repository (it can be in any git hosting service), containing the code and a Readme how to run the api
Optionally you can also provide a Dockerfile, or docker-compose file.
The persistance layer can be as simple as sqlite3 or any other opensource database
The exercise is timeboxed. You should spend less than 4 hours in total.

Some tips:
 - write some tests
 - make sure you put efforts on the commits (message and changes)
 - we will have an hour skype session to talk about the code/decisions after it.


Should you have any questions, contact jose@deliveryhero.com directly.
