# This file geo_location is created by lincan for Project uuloong-strategy
# on a date of 8/11/16 - 2:07 PM

import os
import geoip2.database

__author__ = "lincan"
__copyright__ = "Copyright 2016, The uuloong-strategy Project"
__version__ = "0.1"
__maintainer__ = "lincan"
__status__ = "Production"

base_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.pardir, os.pardir)
config_dir = os.path.join(base_dir, "GeoLite2-Country.mmdb")

geo_client = geoip2.database.Reader(config_dir)


class GeoLocation:
    def __init__(self, ip):
        self.client_ip = ip

        if self.client_ip == "127.0.0.1":
            self.country_code = "CN"
            return

        try:
            self.geo_location = geo_client.country(self.client_ip)
            self.country_code = self.geo_location.country.iso_code

        except ValueError:
            self.country_code = "Default"

    @property
    def location(self):
        return self.country_code
