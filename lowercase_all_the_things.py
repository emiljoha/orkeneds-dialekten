import glob
import os
from bs4 import BeautifulSoup as BS
import codecs

def lower(element, attribute: str):
    if element.has_attr(attribute):
        element[attribute] = element[attribute].lower()

if __name__ == '__main__':
    files = glob.glob("content/www/**/*", recursive=True)
    files.sort()
    for file in files:
        if '.' in file:
            os.renames(file, file.lower())
    for file in glob.glob("content/www/**/*.htm", recursive=True):
        html = BS(codecs.open(file, 'r', 'cp1257').read(), 'html.parser')
        des = html.descendants
        for element in html.descendants:
            if not isinstance(element, str):
                lower(element, 'href')
                lower(element, 'src')
        codecs.open(file, 'w', 'utf-8').write(html.prettify())
