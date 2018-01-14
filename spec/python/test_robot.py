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

        self.bands_path = os.path.dirname(__file__) + '/bands_test.txt'
        self.container = bands_container.BandsContainer(self.bands_path)
        self.bands_list = self.container.get_bands_list_names()
        
    @pytest.mark.skip(reason=LONG_TEST)
    def test_grab_els_from_metallum_bulk(self):
        num_els_expected = 3
        els_expected = [
            dict(city='örebro', country='sweden', genre='doom metal/psychedelic hard rock'),
            dict(city='olympia, washington', country='united states', genre='black metal'),
            dict(city='riihimäki/tampere', country='finland', genre='melodic death/power metal with eastern folk influences'),
            dict(city='linköping', country='sweden', genre='blackened thrash/speed metal'),
            dict(city='sankt oswald-riedlhütte, bavaria', country='germany', genre='pagan/folk metal'),
            dict(city='kouvola/myrskylä', country='finland', genre='melodic death metal'),
            dict(city='großthiemig, brandenburg', country='germany', genre='black metal'),
            dict(city='kristianstad-sölvesborg', country='sweden', genre='melodic death metal'),
            dict(city='bielefeld, north rhine-westphalia', country='germany', genre='symphonic metal'),
            dict(city='umeå', country='sweden', genre='melodic death metal')
        ]

        els_actual = self.robot.grab_els_from_metallum_bulk(self.bands_list)

        for item in zip(els_expected, els_actual):
            expected, actual = item
            shared_items = set(expected.items()) & set(actual.items())
            assert len(shared_items) == num_els_expected

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

