# encoding: UTF-8

from lxml import html
import requests

URL = "https://32blanche.lecointreparis.com/LP"


def get_menu():
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    tds = tree.xpath('//div[@class="pos20"]/descendant::td')
    # Remove "Menu du Jour"
    tds = tds[1:]

    menu = []
    cpt = -1
    for td in tds:
        if td.text is not None:
            if is_section(td):
                cpt += 1
                menu.append({"name": td.text, "sub": []})
            else:
                menu[cpt]['sub'].append(td.text)
    return menu


def is_section(td):
    id_has_len_5 = len(td.get('id')) == 5
    text_is_short = len(td.text) < 10
    is_pdc = td.text.lower() == "plat du chef"
    return (id_has_len_5 and text_is_short) or is_pdc
