import sys
import os
import json
import requests

dir = os.path.dirname(os.path.abspath(__file__))

FB_APP_ID = 'FB_APP_ID'
FB_APP_SECRET = 'FB_APP_SECRET'
FB_API_ACCESS_TOKEN = 'FB_API_ACCESS_TOKEN'
FB_API_URL = 'https://graph.facebook.com/oauth/access_token?'
FB_API_GRANT_TYPE = 'client_credentials'

VARIABLES_PATH = os.path.join(dir, '../../../variables.env')

def get_fb_vars(path=VARIABLES_PATH):
    fb_app_info = {
        'id': '',
        'secret': '',
        'access_token': ''
    }

    with open(path, 'r') as f:
        for line in f:
            s = line.split('=')

            key = s[0]
            val = s[1][:-1]

            if key == FB_APP_ID:
                fb_app_info['id'] = val
            elif key == FB_APP_SECRET:
                fb_app_info['secret'] = val
            elif key == FB_API_ACCESS_TOKEN:
                fb_app_info['access_token'] = val

    return fb_app_info



def get_fb_access_token():
    fb_vars = get_fb_vars(VARIABLES_PATH)

    payload = {
        'grant_type': FB_API_GRANT_TYPE, 
        'client_id': fb_vars['id'],
        'client_secret': fb_vars['secret']
    }

    resp = requests.post(FB_API_URL, params = payload)
    json_resp = json.loads(resp.text)

    try:
        token = json_resp['access_token']
    except:
        token = json_resp['type']

    return token



def get_db_config(path):
    config = {}
    with open(path, 'r') as f:
        for line in f:
            s = line.split('=')
            key = s[0]
            val = s[1]

            if key == "DB_CONFIG": 
                v_split = val.split(',')

                for el in v_split:
                    param = el.split(':')
                    field = param[0]
                    field_val = param[1].replace('\n', '')

                    if field == 'user':
                        config['user'] = field_val
                    elif field == 'password':
                        config['password'] = field_val
                    elif field == 'database':
                        config['database'] = field_val
                    elif field == 'host':
                        config['host'] = field_val

    return config



def retrieve_fb_access_token(path):
    token = ''
    with open(path, 'r') as f:
        for line in f:
            split = line.split('=')
            key = split[0]
            val = split[1]

            if key == FB_API_ACCESS_TOKEN:
                token = val[:-1]

    return token





def store_fb_access_token():
    token = get_fb_access_token()

    already_stored = False
    with open(VARIABLES_PATH, 'r+') as f:
        for line in f:
            split = line.split('=')
            key = split[0]
            val = split[1]
        
            if key == FB_API_ACCESS_TOKEN and val == token:
                already_stored = True

        if already_stored == False:
            line = '{0}={1}\n'.format(FB_API_ACCESS_TOKEN, token)
            f.write(line)



def store_var_in_env(key, val, path):
    line_to_append = '{0}={1}\n'.format(key,val)
    line_already_in_file = False

    with open(path, 'r+') as f:
        for line in f:
            if line == line_to_append:
                line_already_in_file = True

        if line_already_in_file == False:
            f.write(line_to_append)
    
