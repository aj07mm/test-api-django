# Test Api Django

[![Build Status](http://ec2-34-210-79-92.us-west-2.compute.amazonaws.com:8080/buildStatus/icon?job=test-api-django)](http://ec2-34-210-79-92.us-west-2.compute.amazonaws.com:8080/job/test-api-django/)

How to run:

```
make setup
make run
```

Running tests:
```
make test
```

login:

	username: admin
	password: 123

---

# SPECS



1.

A basic (tested) Flask app (or Django if you prefer). 
1.

Write a very simple Flask/Django app which accepts a photo upload via 
a form, and then displays that photo back to the user. You do not need to 
save the uploaded file, simply send it back as the response. Example app 
here (https://pacific-atoll-2556.herokuapp.com/ - it’s a Heroku link 
so it may take a second to startup). 
2.

Write a test for this app which checks that a POST request to the 
upload route correctly returns the uploaded photo as the 
response body. If 
using flask, you may find the flask docs ( 
http://flask.pocoo.org/docs/0.10/testing/ 
) helpful here. 
3.

Push everything to a public github repo. 
2.

Continuous Integration testing for this app 
1.

For this step, your task is to set up public CI for your public repo 
which runs the above test whenever a new commit to master is pushed on 
github. We recommend Travis but here’s a list of other free CI tools. 
2.

Optional bonus points: Autodeploy to a (free) heroku app on a passing 
build. 
3.

Optional bonus points: Getting a “Build passing” badge on your github 
repo that’s updated from your CI.

Once you’ve completed the above, send an email with

1.

Your public github link 
2.

Your heroku instance 
3.

Your CI instance 
4.

Your Resume 
5.

A few availabilities for an interview and we’ll speak!

Best, 
Pascal

