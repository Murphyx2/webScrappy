import os
from bs4 import BeautifulSoup
from requests import get


def get_webpage(url, **kwargs):
    webpage_request = get(url)
    html = webpage_request.text
    soup = BeautifulSoup(html, 'html.parser')
    filename = kwargs.get('filename', None)
    if filename is None:
        title = soup.title.string
        article_name = title.partition('|')[0]
        filename = article_name + '.txt'
    filename = 'scraped_articles/' + filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('<! –– Article URL: ' + url + '-->')
        file.write(soup.prettify())
    return file.name


if __name__ == '__main__':
    medium_url = ('https://medium.com/@pareto_investor/nasa-just-shut-down-quantum-computer-after-something-insane'
                  '-happened-6ddd6ff1d105')
    print(get_webpage(medium_url, filename='Nasa_Article'))
