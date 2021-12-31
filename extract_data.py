import glob
from bs4 import BeautifulSoup as BS
import json
import os

def uttryck(htlm):
    return "Uttryck på dialekt" in htlm.body.text

def dialektord(htlm):
    return "Dialektord" in htlm.body.text

if __name__ == '__main__':
    os.remove('ord.csv')
    os.remove('uttryck.csv')
    for f in glob.glob("content/www/dialekt/sidor/**/*.htm", recursive=True):
        html = BS(open(f, 'r').read(), 'html.parser')

        entry = {
            "audio": html.find('source')['src'],
        }

        if dialektord(html):
            word_tables = html.body.table.find_all('tr')[1].find_all('td')
            dialekt = word_tables[0].font.text.replace('\n', '').strip()
            riks = word_tables[1].font.text.replace('\n', '').strip()
            entry['dialekt'] = dialekt
            entry['riks'] = riks
            with open('ord.csv', 'a') as out:
                out.write(json.dumps(entry) + ",\n")
        elif uttryck(html):
            tables = html.body.find_all('table')
            dialekt = tables[0].find_all('tr')[1].text.replace('\n', '').strip()
            riks = tables[1].find_all('tr')[1].text.replace('\n', '').strip()
            entry['dialekt'] = dialekt
            entry['riks'] = riks
            with open('uttryck.csv', 'a') as out:
                out.write(json.dumps(entry) + "\n")
        else:
            import pdb; pdb.set_trace()
