import sys
import os
import pytest

dir = os.path.dirname(__file__) + '/../../src/api/fb'
sys.path.append(dir)
import auth

TEST_ENV_FILE = './spec/python/variables.env.test'


class TestFbAuth(object):

    def test_get_fb_vars(self):
        fb_app_info_expected = {
            'id': '666',
            'secret': '777',
            'access_token': ''
        }

        fb_app_info_actual = auth.get_fb_vars(TEST_ENV_FILE)

        assert fb_app_info_expected['id'] == fb_app_info_actual['id']
        assert fb_app_info_expected['secret'] == fb_app_info_actual['secret']

    def test_get_fb_access_token(self):
        """
        This test only checks if the auth url still works
        """

        min_chars = 30
        max_chars = 255

        oauth_exception = 'OAuthException'

        fb_access_token = auth.get_fb_access_token()
        len_token = len(fb_access_token)

        assert fb_access_token != oauth_exception
        assert len_token >= min_chars and len_token <= max_chars

    def test_get_db_config(self):
        user_expected = 'admin'
        password_expected = 'password'
        database_expected = 'testdb'
        host_expected = 'localhost' 

        config = auth.get_db_config(TEST_ENV_FILE)

        user_actual = config['user']
        password_actual = config['password']
        database_actual = config['database']
        host_actual = config['host']

        assert user_expected == user_actual
        assert password_expected == password_actual
        assert database_actual == database_actual
        assert host_expected == host_actual

    def test_retrieve_google_api_key(self):
        google_api_key_expected = 'nbtui45yw47threugiwe4y63408673'
        KEY = 'GOOGLE_API_KEY'
        
        auth.store_var_in_env(KEY, google_api_key_expected, TEST_ENV_FILE)
        
        google_api_key_actual = auth.retrieve_google_api_key(TEST_ENV_FILE)
        
        assert google_api_key_expected == google_api_key_actual

    def test_retrieve_fb_access_token(self):
        fb_access_token_expected = '888'
        KEY = 'FB_API_ACCESS_TOKEN'

        auth.store_var_in_env(KEY, fb_access_token_expected, TEST_ENV_FILE)

        fb_access_token_actual = auth.retrieve_fb_access_token(TEST_ENV_FILE)

        assert fb_access_token_expected == fb_access_token_actual

    def test_store_var_in_env(self):
        key_expected = 'CATS'
        val_expected = '1337'

        auth.store_var_in_env(key_expected, val_expected, TEST_ENV_FILE)
       
        found = False
        with open(TEST_ENV_FILE, 'r') as f:
            for line in f:
                if line == 'CATS=1337\n':
                    found = True

        assert found == True

