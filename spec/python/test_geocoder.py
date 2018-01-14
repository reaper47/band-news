import sys
import os
dir = ''.join([os.path.dirname(__file__), '/../../src/api'])
sys.path.append(dir)
import geocoder_helpers
import pytest


class TestGeocoderHelpers(object):

    def setup(self):
        pass

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

        geo_actual = geocoder_helpers.fetch_geo_data_for_db(place)

        assert geo_expected['housenumber'] == geo_actual['housenumber']
        assert geo_expected['street'] == geo_actual['street']
        assert geo_expected['city'] == geo_actual['city']
        assert geo_expected['state'] == geo_actual['state']
        assert geo_expected['country_short'] == geo_actual['country_short']
        assert geo_expected['country_long'] == geo_actual['country_long']
        assert geo_expected['postal'] == geo_actual['postal']
        assert geo_expected['lat'] == geo_actual['lat']
        assert geo_expected['lng'] == geo_actual['lng']
        assert geo_expected['address'] == geo_actual['address']

    def test_fetch_geo_data_for_db_sweden(self):
        place = 'stockholm, sweden'

        geo_expected = {
                'city': "stockholm",
                'state': 'stockholm county',
                'country_short': 'se',
                'country_long': 'sweden',
                'lat': 59.32932349999999,
                'lng': 18.0685808,
                'address': "stockholm, sweden"
        }

        geo_actual = geocoder_helpers.fetch_geo_data_for_db(place)

        assert 'housenumber' not in geo_actual
        assert 'street' not in geo_actual
        assert geo_expected['city'] == geo_actual['city']
        assert geo_expected['state'] == geo_actual['state']
        assert geo_expected['country_short'] == geo_actual['country_short']
        assert geo_expected['country_long'] == geo_actual['country_long']
        assert 'postal' not in geo_actual
        assert geo_expected['lat'] == geo_actual['lat']
        assert geo_expected['lng'] == geo_actual['lng']
        assert geo_expected['address'] == geo_actual['address']




