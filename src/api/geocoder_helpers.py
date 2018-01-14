import geocoder
import pycountry


def fetch_countries_for_db():
    countries_list = []

    pycountries = list(pycountry.countries)
    
    for country in pycountries:
        numeric = int(country.numeric)
        alpha_2 = country.alpha_2.lower()
        name = country.name.lower()

        countries_list.append((numeric, alpha_2, name))

    return countries_list


def fetch_geo_data_for_db(place):
    geodata = {}

    fields = [
        'housenumber', 'street', 'city', 'state',
        'country_long', 'country_short',
        'postal', 'lat', 'lng', 'address'
    ]

    data = geocoder.google(place).json

    for field in fields:
        if field == 'country_short':
            geodata[field] = data['raw']['political']['short_name'].lower()
        elif field == 'country_long':
            geodata[field] = data['raw']['political']['long_name'].lower()
        elif field in data:
            val = data[field]
            
            if field == 'housenumber':
                val = int(val)

            if field == 'lat' or field == 'lng':
                val = float(val)

            if type(val) is str:
                val = val.lower()

            geodata[field] = val

    return geodata
