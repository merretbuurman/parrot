FROM python:2.7.15-alpine3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["parrot_api.py"]

# TODO: Not run as root!

# docker build -t flask-sample-one:20180822 .
# docker run --rm  --name flask_fake_import_manager -d -p 5000:5000 -v /home/.../flasklogs:/app/logs flask-sample-one:20180822
