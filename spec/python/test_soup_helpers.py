import sys
import os
dir = os.path.dirname(__file__) + '/../../src/api'
sys.path.append(dir)
import soup_helpers


class TestSoupHelpers(object):

    def setup(self):
        self.test_url = 'https://www.metal-archives.com/bands/wulfgar'
        self.test_url2 = 'https://www.metal-archives.com/bands/amon_amarth'

        self.test_soup = soup_helpers.brew_soup_from_url(self.test_url)
        self.test_soup2 = soup_helpers.brew_soup_from_url(self.test_url2)

    def test_brew_soup_from_url(self):
        soup_actual = soup_helpers.brew_soup_from_url(self.test_url)

        assert len(soup_actual.text) > 0

    def test_is_band_active_metallum_active(self):
        url_active_band = 'https://www.metal-archives.com/bands/Witchcraft/18938'
        status_expected = True

        status_actual = soup_helpers.is_band_active_metallum(url_active_band)

        assert status_expected == status_actual

    def test_is_band_active_metallum_inactive(self):
        url_inactive_band = 'https://www.metal-archives.com/bands/Witchcraft/110731'
        status_expected = False

        status_actual = soup_helpers.is_band_active_metallum(url_inactive_band)

        assert status_expected == status_actual

    def test_get_genre_from_soup_metallum(self):
        genre_expected = 'melodic death metal'

        genre_actual = soup_helpers.get_genre_from_soup_metallum(self.test_soup2)

        assert genre_expected == genre_actual

    def test_get_loc_from_soup_metallum(self):
        loc_expected = ('stockholm', 'sweden')

        loc_actual = soup_helpers.get_loc_from_soup_metallum(self.test_soup2)
        
        for item in zip(loc_expected, loc_actual):
            expected, actual = item

            assert expected == actual

    def test_url_from_atags_soup_metallum(self):
        country_code = '(DE)'
        url_expected = 'https://www.metal-archives.com/bands/Wulfgar/84862'

        url_actual = soup_helpers.url_from_atags_soup_metallum(self.test_soup, country_code)

        assert url_expected == url_actual


