#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search1.py

# (The Google API originally used in this example now requires API keys,
#  so here's an alternative that calls openstreetmap.org.)

import geocoder

def main():
    address = 'Petronas Towers'
    g = geocoder.osm(address)

    location = g.latlng
    print(f'lattitude :{location[0]}\nlongitude :{location[1]}')

    print(f"house number: {g.housenumber}\nstreet: {g.street}\ncity: {g.city}\nstate: {g.state}\npostal: {g.postal}\ncountry: {g.country}\n")



if __name__ == '__main__':
    main()