import sys
import os
dir = os.path.dirname(__file__) + '/../../src/api'
sys.path.append(dir)
import bands_container
import pytest


class TestBandsContainer(object):

    def setup(self):
        self.bands_container = bands_container.BandsContainer()
        self.bands_path = os.path.dirname(__file__) + '/bands_test.txt'

    def test_load_bands(self):
        bands_expected = {
            'names': [
                'witchcraft(SE)', 'wolves_in_the_throne_room', 'whispered',
                'witchery(SE)', 'wolfchant', 'wolfheart(FI)', 'wulfgar(DE)',
                'wulfgar(SE)', 'xandria', 'zonaria'
            ],
            'fb': [
                'witchcraft', 'wolvesinthethroneroom', 'pages/Whispered/152411565720',
                'officialwitchery', 'pages/Wolfchant/168334363212064',
                'WolfheartRealm', 'WulfgarBlackMetal', 'wulfgarband',
                'xandriaofficial', 'ZonariaOfficial'
            ]
        }

        bands_actual = self.bands_container.load_bands(self.bands_path);
        print("actual bands: ", bands_actual) 
        names_diff = set(bands_expected['names']) & set(bands_actual['names'])
        fb_diff = set(bands_expected['fb']) & set(bands_actual['fb'])

        assert len(names_diff) == len(bands_expected['names'])
        assert len(fb_diff) == len(bands_expected['fb'])
