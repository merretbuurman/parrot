'''
This module contains a little flask server that
simply accepts POST and GET requests and logs the content
to a log file.

Used as a fake REST API to check whether asynchronous
processes  properly notify their completion.

'''

from flask import Flask, request
app = Flask(__name__)


# Create log dir
import os
try:
    os.mkdir('logs')
except OSError as e:
    if 'File exists:' in str(e):
        pass
    else:
        raise e

# Configure logging to console and to log file
import sys
import logging
root = logging.getLogger()
root.setLevel(logging.WARN) # TODO: does not work...
ha = logging.StreamHandler(sys.stdout)
ha.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(ha)
fh = logging.FileHandler('logs/log.txt', mode='w')
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(fh)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

'''
Usage on localhost:

POST with JSON content:
curl -v -X POST -H "Content-Type: application/json" --data '{"foo":"xyz","bar":"xyz"}' localhost:5000/what/ever/

POST with form content:
curl -v -X POST localhost:5000/what/ever/ --data foo=xyz --data bar=xyz

GET with params:
curl -v -X GET  localhost:5000/what/ever?foo=xyz&bar=xyz 
curl -v -G --data "foo=xyz&bar=xyz" localhost:5000/what/ever
'''


# Catch all
# https://stackoverflow.com/questions/45777770/catch-all-routes-for-flask#45777812
# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):

    LOGGER.info('(0) Got path "%s"' % path)

    if request.method == 'POST':
        LOGGER.info('(1) Received post from "%s"', request.remote_addr)

        # json
        json_content = request.get_json()
        LOGGER.info('(2) Contains JSON content: %s', json_content)

        # form
        form_content = []
        for k,v in request.form.items():
            form_content.append('%s=%s' % (k, v))
        if len(form_content) == 0:
            form_content = None
        else:
            form_content = '; '.join(form_content)
        LOGGER.info('(3) Contains form content: %s', form_content)

        # Response:
        return 'Received and accepted POST from %s to %s' % (request.remote_addr, path)

    if request.method == 'GET':

        LOGGER.info('(1) Received get from "%s"', request.remote_addr)

        params_content = []
        for k,v in request.args.items():
            params_content.append('%s=%s' % (k, v))
        if len(params_content) == 0:
            params_content = None
        else:
            params_content = '; '.join(params_content)
        LOGGER.info('(2) Contains param content: %s', params_content)

        return 'Received and accepted GET from %s to %s' % (request.remote_addr, path)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
