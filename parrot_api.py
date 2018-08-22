from flask import Flask, request
app = Flask(__name__)

import sys
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
this_one = logging.getLogger('parrot_api')
this_one.setLevel(logging.INFO)
ha = logging.StreamHandler(sys.stdout)
ha.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(ha)
fh = logging.FileHandler('log.txt', mode='w')
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(fh)

LOGGER = logging.getLogger(__name__)

# Usage on localhost:
# curl localhost:5000/what/ever/ -X POST -H "Content-Type: application/json" --data '{"foo":"xyz","bar":"xyz"}'


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
        form_content = ''
        for k,v in request.form:
            form_content = ('%s, %s=%s' % (form_content, k, v))
        LOGGER.info('(3) Contains form content: %s', form_content)

        return 'all righty'

    if request.method == 'GET':
        msg =  "Get is not implemented..."
        LOGGER.info(msg)
        return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
