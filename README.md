# Parrot

This module contains a little flask server that
simply accepts POST and GET requests and logs the content
to a log file.

Used as a fake REST API to check whether asynchronous
processes  properly notify their completion.


## Run as python module:

```
# Make virtual env
virtualenv venv
source venv/bin/activate

# Install Flask
pip install Flask

# Run app
python parrot-api.py
```

## Run as docker container:

```
mkdir app
cp Dockerfile app/
cp requirements.txt app/
cp parrot_api.py app/

cd app
docker build -t flask-parrot:latest .
docker run --rm  --name parrot -d -p 5000:5000 flask-parrot:latest
```

Like this, the log will be stored inside the container in
app/logs/log.txt. It is easier to view them if you bind-mount them:

```
mkdir app
cp Dockerfile app/
cp requirements.txt app/
cp parrot_api.py app/

cd app
mkdir flask_logs
docker build -t flask-parrot:latest .
docker run --rm  --name parrot -d -v /path/to/app/flasklogs:/app/logs -p 5000:5000 flask-parrot:latest
```

## Disclaimer

Note that this is a devel/debug module, it does not
contain any security config and should not be run in
production.

## Usage

Test it on localhost, using curl:

```
# POST with JSON content:
curl -v -X POST -H "Content-Type: application/json" --data '{"foo":"xyz","bar":"xyz"}' localhost:5000/what/ever/

# POST with form content:
curl -v -X POST localhost:5000/what/ever/ --data foo=xyz --data bar=xyz

# GET with params:
curl -v -X GET  localhost:5000/what/ever?foo=xyz&bar=xyz 
curl -v -G --data "foo=xyz&bar=xyz" localhost:5000/what/ever
```

The contents of these calls should now be visible in the
bind-mounted log file: `vi /path/to/app/flasklogs/log.txt`

```
2018-08-22 12:48:19,544 - __main__ - INFO - (0) Got path "what/ever/"
2018-08-22 12:48:19,544 - __main__ - INFO - (1) Received post from "127.0.0.1"
2018-08-22 12:48:19,546 - __main__ - INFO - (2) Contains JSON content: {u'foo': u'xyz', u'bar': u'xyz'}
2018-08-22 12:48:19,547 - __main__ - INFO - (3) Contains form content: None
2018-08-22 12:48:29,834 - __main__ - INFO - (0) Got path "what/ever/"
2018-08-22 12:48:29,835 - __main__ - INFO - (1) Received post from "127.0.0.1"
2018-08-22 12:48:29,836 - __main__ - INFO - (2) Contains JSON content: None
2018-08-22 12:48:29,838 - __main__ - INFO - (3) Contains form content: foo=xyz; bar=xyz
2018-08-22 12:48:41,145 - __main__ - INFO - (0) Got path "what/ever"
2018-08-22 12:48:41,145 - __main__ - INFO - (1) Received get from "127.0.0.1"
2018-08-22 12:48:41,146 - __main__ - INFO - (2) Contains param content: foo=xyz
2018-08-22 12:49:10,559 - __main__ - INFO - (0) Got path "what/ever"
2018-08-22 12:49:10,560 - __main__ - INFO - (1) Received get from "127.0.0.1"
2018-08-22 12:49:10,560 - __main__ - INFO - (2) Contains param content: foo=xyz; bar=xyz
2018-08-22 12:49:12,733 - __main__ - INFO - (0) Got path "what/ever"
2018-08-22 12:49:12,734 - __main__ - INFO - (1) Received get from "127.0.0.1"
2018-08-22 12:49:12,735 - __main__ - INFO - (2) Contains param content: foo=xyz; bar=xyz
```