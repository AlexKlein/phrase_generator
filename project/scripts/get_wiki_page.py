"""
Getting random wiki themes with links on sources.

"""
import os
import random
from datetime import datetime

import requests
import urllib3 as urllib3

import settings as config
from storage.themes.list_of_themes import people
from storage.themes.list_of_themes import literary_works
from storage.themes.list_of_themes import films
from storage.themes.list_of_themes import tv_shows
from storage.themes.list_of_themes import themes
from storage.themes.list_of_themes import places


API_URL = config.API_URL
API_VERSION = config.API_VERSION
USER_AGENT = config.USER_AGENT


urllib3.disable_warnings()
os.environ['CURL_CA_BUNDLE'] = ""


def get_theme():
    theme_number = str(random.randint(1, 6))
    theme_map = {
        '1': people,
        '2': literary_works,
        '3': films,
        '4': tv_shows,
        '5': themes,
        '6': places
    }
    return theme_map.get(theme_number)


def get_page_id(session, query):
    search_item = query[random.randint(1, len(query))]
    params = {
        'list': 'search',
        'srprop': '',
        'srlimit': 10,
        'srsearch': search_item,
        'format': 'json',
        'action': 'query'
      }
    headers = {
        'User-Agent': USER_AGENT
      }
    json_data = session.get(
        API_URL,
        params=params,
        headers=headers
    ).json()
    return json_data['query']['search'][random.randint(1, len(json_data['query']['search']))]['pageid']


def get_page(session, page_id):
    params = {
        'action': 'parse',
        'format': 'json',
        'pageid':  str(page_id)
      }

    return session.get(
        API_URL,
        params=params
    ).json()


def start_up():
    session = requests.Session()
    query = get_theme()
    page_id = get_page_id(session, query)
    json_data = get_page(session, page_id)
    try:
        title =  str(json_data['parse']['displaytitle']).replace('<i>', '').replace('</i>', '')
    except Exception as e:
        print(e)
        title = ''

    try:
        link = str(json_data['parse']['iwlinks'][0]['url'])
    except Exception as e:
        print(e)
        link = ''

    try:
        externallinks = json_data['parse']['externallinks'][:5]
    except Exception as e:
        print(e)
        externallinks = ''

    json_return = {
        'meta':
            {
                'api_version': API_VERSION,
                'code': 200,
                'issue_date': datetime.strftime(datetime.now(), '%Y-%m-%d')
            },
        'parse':
            {
                'title': title,
                'link': link,
                'externallinks': externallinks

            }
    }
    return json_return
