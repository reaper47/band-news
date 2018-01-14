import sys
import os
dir = ''.join([os.path.dirname(__file__), '/../../src/api'])
sys.path.append(dir)
import robot
import bands_container
import pytest

LONG_TEST = 'enable only for periodic checks'


class TestRobot(object):

    def setup(self):
        self.robot = robot.Robot()
        self.container = bands_container.BandsContainer()
        self.bands_path = os.path.dirname(__file__) + '/bands_test.txt'
        self.bands_list = self.container.load_bands(self.bands_path)['names']

    @pytest.mark.skip(reason=LONG_TEST)
    def test_grab_genre_from_metallum_bulk(self):
        el = 'genre'

        genres_expected = [
            'Doom Metal/Psychedelic Hard Rock',
            'Black Metal',
            'Melodic Death/Power Metal with Eastern Folk influences',
            'Blackened Thrash/Speed Metal',
            'Pagan/Folk Metal',
            'Melodic Death Metal',
            'Black Metal',
            'Melodic Death Metal',
            'Symphonic Metal',
            'Melodic Death Metal'
         ]

        genres_actual = self.robot.grab_els_from_metallum_bulk(self.bands_list, el)

        for item in zip(genres_expected, genres_actual):
            expected, actual = item

            assert expected == actual

    @pytest.mark.skip(reason=LONG_TEST)
    def test_grab_loc_from_metallum_bulk(self):
        el = 'loc'

        locs_expected = [
            ('Örebro', 'Sweden'),
            ('Olympia, Washington', 'United States'),
            ('Riihimäki/Tampere', 'Finland'),
            ('Linköping', 'Sweden'),
            ('Sankt Oswald-Riedlhütte, Bavaria', 'Germany'),
            ('Kouvola/Myrskylä', 'Finland'),
            ('Großthiemig, Brandenburg', 'Germany'),
            ('Kristianstad-Sölvesborg', 'Sweden'),
            ('Bielefeld, North Rhine-Westphalia', 'Germany'),
            ('Umeå', 'Sweden')
        ]

        locs_actual = self.robot.grab_els_from_metallum_bulk(self.bands_list, el)

        for item in zip(locs_expected, locs_actual):
            item_expected, item_actual = item

            for subitem in zip(item_expected, item_actual):
                sub_expected, sub_actual = subitem

                assert sub_expected == sub_actual


    def test_get_crawl_delay_website(self):
        crawl_delay_metallum_expected = 3.0

        website = self.robot.metal_archives_base
        crawl_delay_metallum_actual = self.robot.get_crawl_delay_website(website)

        assert crawl_delay_metallum_expected == crawl_delay_metallum_actual

    def test_read_robots_txt(self):
        base_url = 'https://www.metal-archives.com'
        initial_modified_time = self.robot.robotparser.mtime()

        self.robot.read_robots_txt(base_url)

        time_after_read = self.robot.robotparser.mtime()

        assert time_after_read > initial_modified_time
