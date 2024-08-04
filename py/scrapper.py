import requests
from bs4 import BeautifulSoup


url = "https://www.numbeo.com/cost-of-living/in/"


def scrap_website_structure(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(type(soup))
    return soup


def try_to_find_city(url: str) -> bool:
    """
    Checks whether requested city exists

    Args:
        url (str): generated url to the requested city
    """
    soup = scrap_website_structure(url)
    div_tags = soup.find_all('div', {'class': 'innerWidth'})
    for div_tag in div_tags:
        h1_tags = div_tag.find_all('h1')
        for h1 in h1_tags:
            if "Cannot find city" in h1.get_text():
                return False
    return True


def create_link_to_city_info(city_name:str) -> str:
    """Creates link to city if it exists

    Returns:
        str: link to city or '' in case of fail
    """
    link_to_city = url + city_name + "/"
    if try_to_find_city(link_to_city):
        return link_to_city
    else:
        return ""

# if __name__ == "__main__":
#     scrap_website_structure("https://www.numbeo.com/cost-of-living/in/Potsdam")