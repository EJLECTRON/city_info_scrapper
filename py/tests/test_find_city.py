import pytest

import scrapper

url = "https://www.numbeo.com/cost-of-living/in/"


def test_try_to_find_city_true():
    """
    Function that checks existing cities
    """
    city_names = ["Potsdam", "Berlin", "Munich", "Stuttgart"]
    for city_name in city_names:
        assert scrapper.create_link_to_city_info(city_name) == url + city_name + "/"
        

def test_try_to_find_city_false():
    """
    Function that checks existing cities
    """
    city_names = ["P]otsdam", "Berlidfqewfn", "Muwefnich", "Stuttgawefrt"]
    for city_name in city_names:
        assert scrapper.create_link_to_city_info(city_name) == ""
