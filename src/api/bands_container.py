class BandsContainer(object):

    def __init__(self):
        pass

    def load_bands(self, path):
        bands = {'names': [], 'fb': []}

        with open(path, 'r') as f:
            for line in f:
                s = line.split('=')
                name = s[0]
                fb_name = s[1].replace('\n', '')
                
                bands['names'].append(name)
                bands['fb'].append(fb_name)
        
        return bands

    


        
