import sys
import os
dir = os.path.dirname(os.path.realpath(__file__))
BANDS_TXT_PATH = os.path.join(dir, 'bands.txt')


class BandsContainer(object):

    def __init__(self, bands_file_path):
        self.path = bands_file_path
        self.bands_list = self.load_bands()
    
    def get_bands_list_fb(self):
        return self.bands_list['fb']

    def get_bands_list_names(self):
        return self.bands_list['names']

    def load_bands(self):
        bands = {'names': [], 'fb': []}

        with open(self.path, 'r') as f:
            for line in f:
                s = line.split('=')
                name = s[0]
                fb_name = s[1].replace('\n', '')
                
                bands['names'].append(name)
                bands['fb'].append(fb_name)
        
        return bands
  
