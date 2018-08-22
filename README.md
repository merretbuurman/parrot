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

