import os

from flask import Flask

from scripts import get_wiki_page

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = Flask(__name__)


@app.route('/')
def get_page():
    return get_wiki_page.start_up()


def start_up(host, port):
    app.run(host=host, port=port, debug=True)
