import glob
import os
from bs4 import BeautifulSoup as BS
from bs4 import Tag


if __name__ == '__main__':
    for file in glob.glob("content/www/**/*.htm", recursive=True):
        html = BS(open(file, 'r').read(), 'html.parser')
        bgsound = html.find('bgsound')
        mouth_image = html.find('img', {'alt': 'Ljud'})
        if bgsound is not None and mouth_image is not None:
            print(file)
            audio = Tag(name='audio', attrs={'controls': None})
            source = Tag(name='source', attrs={'src': bgsound['src'], 'type': 'audio/wav'})
            audio.insert(0, source)
            mouth_image.replaceWith(audio)
            bgsound.decompose()
            open(file, 'w').write(html.prettify())
