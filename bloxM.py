from bs4 import BeautifulSoup
import requests

blox = requests.get('https://blox-fruits.fandom.com/wiki/Blox_Fruits_"Stock"').text
soup = BeautifulSoup(blox, 'html.parser')

stock = []
for table in soup.find_all('table'):
    for t in table.find_all("th"):
        stock.append(t.text)

for i, el in enumerate(stock):
    if el == '\n':
        del stock[i]

current = stock[:stock.index('\n\n')]
current = current[2:]
last = stock[stock.index('Last Stock\n') + 1:]
last = last[:last.index('\n\n')]
past = stock[stock.index('Before Last Stock\n') + 1:]
past = past[:past.index('\n\n')]

for elements in current:
    current[current.index(elements)] = elements.replace('\n', '')
for elements in last:
    last[last.index(elements)] = elements.replace('\n', '')
for elements in past:
    past[past.index(elements)] = elements.replace('\n', '')

CLP = {"current": current, "last": last, "past": past}


class bloxM:
    def currentStock(self=''):
        rn = []
        for ele in CLP["current"]:
            rn.append(ele.strip())
        trat(rn)
        return rn

    def lastStock(self=''):
        rn = []
        for elee in CLP["last"]:
            rn.append(elee.strip())
        trat(rn)
        return rn

    def pastStock(self=''):
        rn = []
        for eleee in CLP["past"]:
            rn.append(eleee.strip())
        trat(rn)
        return rn


def trat(l):
    for elements in l:
        if str(elements).startswith('Kilo'):
            l[l.index(elements)] = '<:Kilo:1076183921085128844> ' + l[l.index(elements)]
        if str(elements).startswith('Spike'):
            l[l.index(elements)] = '<:Spike:1076184349906571274> ' + l[l.index(elements)]
        if str(elements).startswith('Chop'):
            l[l.index(elements)] = '<:Chop:1076184038890553394> ' + l[l.index(elements)]
        if str(elements).startswith('Spring'):
            l[l.index(elements)] = '<:Spring:1076184089683562616> ' + l[l.index(elements)]
        if str(elements).startswith('Bomb'):
            l[l.index(elements)] = '<:Bomb:1076184118724931685> ' + l[l.index(elements)]
        if str(elements).startswith('Smoke'):
            l[l.index(elements)] = '<:Smoke:1076184320533872782> ' + l[l.index(elements)]
        if str(elements).startswith('Flame'):
            l[l.index(elements)] = '<:Flame:1076184381292548217> ' + l[l.index(elements)]
        if str(elements).startswith('Ice'):
            l[l.index(elements)] = '<:Ice:1076184421796958218> ' + l[l.index(elements)]
        if str(elements).startswith('Sand'):
            l[l.index(elements)] = '<:Sand:1076184450733441124> ' + l[l.index(elements)]
        if str(elements).startswith('Dark'):
            l[l.index(elements)] = '<:Dark:1076184478130647091> ' + l[l.index(elements)]
        if str(elements).startswith('Revive'):
            l[l.index(elements)] = '<:Revive:1076184500041687121> ' + l[l.index(elements)]
        if str(elements).startswith('Diamond'):
            l[l.index(elements)] = '<:Diamond:1076184559462404116> ' + l[l.index(elements)]
        if str(elements).startswith('Light'):
            l[l.index(elements)] = '<:Light:1076184726060154890> ' + l[l.index(elements)]
        if str(elements).startswith('Love'):
            l[l.index(elements)] = '<:Love:1076184758733770792> ' + l[l.index(elements)]
        if str(elements).startswith('Rubber'):
            l[l.index(elements)] = '<:Rubber:1076184796218269707> ' + l[l.index(elements)]
        if str(elements).startswith('Barrier'):
            l[l.index(elements)] = '<:Barrier:1076184829760118864> ' + l[l.index(elements)]
        if str(elements).startswith('Bird:'):
            l[l.index(elements)] = ':bird: ' + l[l.index(elements)]
        if str(elements).startswith('Dragon'):
            l[l.index(elements)] = '<:Dragon:1076185539763523754> ' + l[l.index(elements)]
        if str(elements).startswith('Human: Buddha'):
            l[l.index(elements)] = '<:Buddha:1076184972567789630>' + l[l.index(elements)]
        if str(elements).startswith('Venom'):
            l[l.index(elements)] = '<:Venom:1076185435308564491>   ' + l[l.index(elements)]
        if str(elements).startswith('Magma'):
            l[l.index(elements)] = '<:Magma:1076184869425643520>   ' + l[l.index(elements)]
        if str(elements).startswith('Rumble'):
            l[l.index(elements)] = '<:Rumble:1076185176540983347>   ' + l[l.index(elements)]
