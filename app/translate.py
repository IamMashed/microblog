import json
import requests
from flask_babel import _
import urllib.parse
from flask import current_app


def translate(text, source_language):
    key = current_app.config['TRANSLATOR_KEY']
    if 'TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    # auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        key,
        urllib.parse.quote_plus(text),
        source_language
    )
    )
    print('I got the following key {}'. format(key))

    if r.status_code != 200:
        return _('Error: the translation service failed.')

    p = json.loads(r.content.decode('utf-8'))
    p = p['text'][0]
    print('trying to parse translation only {}'.format(p))
    return p
