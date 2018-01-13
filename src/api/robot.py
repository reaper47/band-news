from bs4 import BeautifulSoup
import time
from datetime import datetime
import urllib.parse
import urllib.robotparser
import urllib.request
import soup_helpers


class Robot(object):

    def __init__(self):
        self.metal_archives_base = 'https://www.metal-archives.com/'
        self.robotparser = urllib.robotparser.RobotFileParser()

    def get_crawl_delay_website(self, website):
        """ add condition when no crawl_delay"""
        robot_url = urllib.parse.urljoin(website, 'robots.txt')

        with urllib.request.urlopen(robot_url) as resp:
            text = resp.read().decode('utf-8')

        robots_lines = text.split('\n')
        for line in robots_lines:
            if 'Crawl-delay' in line:
                crawl_delay = line
                break

        crawl_delay_seconds = float(crawl_delay.split(':')[-1].strip())

        return crawl_delay_seconds

    def grab_els_from_metallum_bulk(self, bands_list, el):
        base = self.metal_archives_base

        self.read_robots_txt(base)
        
        can_fetch_base = self.robotparser.can_fetch('*', base)
        can_fetch_bands = self.robotparser.can_fetch('*', base + 'bands/')

        elements = []
        if can_fetch_base and can_fetch_bands:
            crawl_delay = self.get_crawl_delay_website(base)

            for band in bands_list:
                multiple_band_results = band.find('(')
                if multiple_band_results != -1:
                    country_code = ''.join(['(', band[band.find('(')+1:band.find(')')], ')'])
                    band = band.split('(')[0]

                url = urllib.parse.urljoin(base, 'bands/' + band)
                soup = soup_helpers.brew_soup_from_url(url)
                partial_crawl_start = datetime.now()
                            
                if multiple_band_results != -1:
                    url = soup_helpers.url_from_atags_soup_metallum(soup, country_code)
                    soup = soup_helpers.brew_soup_from_url(url)
                    partial_craw_start = datetime.now()
                
                if el == 'genre':
                    el_fetched = soup_helpers.get_genre_from_soup_metallum(soup)
                elif el == 'loc':
                    el_fetched = soup_helpers.get_loc_from_soup_metallum(soup)

                elements.append(el_fetched)

                diff = (datetime.now()-partial_crawl_start).total_seconds()
                if diff < crawl_delay: 
                    time.sleep(diff)

        return elements
    
    def read_robots_txt(self, base_url):
        url_robot = urllib.parse.urljoin(base_url, 'robots.txt')
        self.robotparser.set_url(url_robot)
        self.robotparser.read()
        self.robotparser.modified()



