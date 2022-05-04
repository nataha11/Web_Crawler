from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def generate_obj(header, text, date):
    return {
        "header": header,
        "text": text,
        "date": date
    }
    
def parse_page_to_json(src_url):
    
    html = urlopen(src_url)
    bsObj = BeautifulSoup(html, "lxml")

    articles = []

    article_name = bsObj.find("h1", {"class":"article__title"})

    text = ""
    news_text = bsObj.findAll("div", {"class":"article__text"})
    for block in news_text:
        text += block.get_text() + '\n'

    tmp = bsObj.find("div", {"class":"article__info-date"}).a
    unix_timestamp = tmp['data-unixtime']

    articles.append(generate_obj(article_name.get_text(), text.rstrip(), unix_timestamp))

    with open("articles.json", "w") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)
  

def main():
    parse_page_to_json("https://uz.sputniknews.ru/20220504/yurlitsam-razreshili-zanimatsya-mayningom-24351731.html")

if __name__ == '__main__':
    main()




