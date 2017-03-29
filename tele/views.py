from bs4 import BeautifulSoup
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def scrap(request, number):
    z = {}

    url = 'http://www.nccptrai.gov.in/nccpregistry/saveSearchSub.misc'
    r = requests.post(url, data={'phoneno': number})

    plain_text = r.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    table = soup.findAll("table")

    tab = table[2].find_all("tr")

    dict = {}
    dict2 = {}

    for t in tab[2:]:
        val = t.find_all("td")
        a, b, c = val
        dict[a.text] = c.text



    try:
        tab = table[4].findAll("tr", {'class': "heading3"})
        heads =[]
        for t in tab[0].find_all("th"):
            heads.append(t.text)


        tab = table[4].find_all('tr')
        cnt = 0
        for t in tab[2:]:
            value = []
            for val in t.find_all('td'):
                value.append(val.text)
            d = {}
            for k, v in zip(heads, value):
                d[k] = v
            dict2[cnt] = d
            cnt += 1
            value.clear()

        z['Preference History'] = dict2
    except:
        pass

    z['Customer Registration Status'] = dict

    return Response(z)
