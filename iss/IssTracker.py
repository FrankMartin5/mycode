#!/usr/bin/env python3

import requests

url = "http://api.open-notify.org/iss-now.json"

def main():
    res = requests.get(url).json()

    print(res)
    print(type(res))

    longitude = res['iss_position']['longitude']
    latitude = res['iss_position']['latitude']

    print(f"Current location of ISS: Longitude: {longitude} Latitude: {latitude}")

main()