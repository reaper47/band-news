from bs4 import BeautifulSoup
import urllib.request


def brew_soup_from_url(url):
        req = urllib.request.urlopen(url)
        status = req.getcode()

        html = ''
        if status == 200:
            html = req.read().decode('utf-8')
                    
        return BeautifulSoup(html, 'html.parser')



"""
*
* Helpers for: https://www.metal-archives.com
*
"""
def is_band_active_metallum(url):    
    soup = brew_soup_from_url(url)

    dts = soup.find_all('dt')
    dds = soup.find_all('dd')

    for item in list(zip(dts, dds)):
        dt, dd = item

        if 'status' in dt.string.lower():
            status = dd.string.lower()
            break
    
    if status == 'active':
        return True

    return False



def get_genre_from_soup_metallum(soup):
    dts = soup.find_all('dt')
    dds = soup.find_all('dd')

    genre = ''
    for item in list(zip(dts, dds)):
        dt, dd = item
            
        if 'genre' in dt.string.lower():
            genre = dd.string.lower()
            break

    return genre



def get_loc_from_soup_metallum(soup):
    dts = soup.find_all('dt')
    dds = soup.find_all('dd')

    city = ''
    country = ''

    for item in list(zip(dts, dds)):
        dt, dd = item

        if 'location' in dt.string.lower():
            city = dd.string.lower()

        if 'country' in dt.string.lower():
            country = dd.string.lower()

    return (city, country)



def url_from_atags_soup_metallum(soup, country_code):
    a_tags = soup.find_all('a')

    url = ''
    for a in a_tags:
        if country_code in a.string:
            band_active = is_band_active_metallum(a['href'])
                            
            if band_active:
                url = a['href']
                break

    return url          

