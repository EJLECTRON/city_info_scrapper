import requests
from bs4 import BeautifulSoup


url = "https://www.numbeo.com/cost-of-living/in/"


def create_link_to_city_info(city_name:str) -> str:
    link_to_city = url + city_name + "/"
    if try_to_find_city(link_to_city):
        return link_to_city
    else:
        return ""


def try_to_find_city(url: str) -> bool:
    """
    Checks whether requested city exists

    Args:
        url (str): generated url to the requested city
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div_tags = soup.find_all('div', {'class': 'innerWidth'})
    for div_tag in div_tags:
        h1_tags = div_tag.find_all('h1')
        for h1 in h1_tags:
            if "Cannot find city" in h1.get_text():
                return False
    return True

