import sys
import os
dir = ''.join([os.path.dirname(__file__), '/../../src/api'])
dir2 = ''.join([os.path.dirname(__file__), '/../../src/api/fb'])
sys.path.append(dir)
sys.path.append(dir2)
import auth
import geocoder_helpers
import pytest


class TestGeocoderHelpers(object):

    def setup(self):
        self.google_api_key = auth.retrieve_google_api_key()

    def test_fetch_countries_for_db(self):
        countries_actual = [
            (533, 'aw', 'aruba'),
            (4, 'af', 'afghanistan'),
            (24, 'ao', 'angola'),
            (660, 'ai', 'anguilla'),
            (248, 'ax', 'åland islands'),
            (8, 'al', 'albania'),
            (20, 'ad', 'andorra'),
            (784, 'ae', 'united arab amirates'),
            (32, 'ar', 'argentina'),
            (51, 'am', 'armenia')
        ]
        
        countries_expected = geocoder_helpers.fetch_countries_for_db()

        count = 0
        for item in zip(countries_expected, countries_actual):
            tuple_expected, tuple_actual = item

            for subitem in zip(tuple_expected, tuple_actual):
                if count == 10:
                    break

                count += 1
                val_expected, val_actual = subitem

                assert val_expected == val_actual       
    
    def test_fetch_geo_data_for_db_qc(self):
        place = '1920 rue Victor-L-Laurin'

        num_els_eq_geo_expected = 10
        geo_expected = {
                'housenumber': 1920,
                'street': 'rue victor l laurin',
                'city': "l'ancienne-lorette",
                'state': 'qc',
                'country_short': 'ca',
                'country_long': 'canada',
                'postal': 'g2e 5y6',
                'lat': 46.81821679999999,
                'lng': -71.36110719999999,
                'address': "1920 rue victor l laurin, l'ancienne-lorette, qc g2e 5y6, canada"
        }

        geo_actual = geocoder_helpers.fetch_geo_data_for_db(place, self.google_api_key)

        shared_items = set(geo_expected.items()) & set(geo_actual.items())

        assert len(shared_items) == num_els_eq_geo_expected

    def test_fetch_geo_data_for_db_sweden(self):
        place = 'stockholm, sweden'

        num_els_eq_geo_expected = 7
        geo_expected = {
                'city': "stockholm",
                'state': 'stockholm county',
                'country_short': 'se',
                'country_long': 'sweden',
                'lat': 59.32932349999999,
                'lng': 18.0685808,
                'address': "stockholm, sweden"
        }

        geo_actual = geocoder_helpers.fetch_geo_data_for_db(place, self.google_api_key)
        
        shared_items = set(geo_expected.items()) & set(geo_actual.items())

        assert len(shared_items) == num_els_eq_geo_expected
       


