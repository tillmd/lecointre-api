#encoding: UTF-8

from lxml import html
import requests
import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def menu():
    URL="https://32blanche.lecointreparis.com/LP"

    page = requests.get(URL)
    tree = html.fromstring(page.content)

    tds = tree.xpath('//div[@class="pos20"]/descendant::td')

    menu = {}
    current_main = ""

    cpt = 1

    for td in tds:
      if (len(td.get('id')) == 5 and len(td.text) < 10) or td.text.lower() == "plat du chef":
        current_main = "%i-%s" % (cpt, td.text)
        menu[current_main] = []
        cpt += 1
      else:
        if td.text.lower() != "menu du jour":
            menu[current_main].append(td.text)
    print menu
    return jsonify(menu)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

