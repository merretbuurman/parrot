FROM python:2.7.15-alpine3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["parrot_api.py"]

# TODO: Not run as root!

# docker build -t flask-parrot:20180822 .
# docker run --rm  --name parrot -d -p 5000:5000 -v /home/.../flasklogs:/app/logs flask-parrot:20180822

