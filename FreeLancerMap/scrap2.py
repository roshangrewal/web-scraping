from bs4 import BeautifulSoup as soup
import requests

urls = []


def crawl(page, msl):
    my_url = msl + "page/" + str(page)
    # my_url="https://einsty.com/hi/category/%E0%A4%9C%E0%A5%80%E0%A4%B5-%E0%A4%B5%E0%A4%BF%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8/page/"+str(page)
    page_html = requests.get(my_url).content
    page_soup = soup(page_html, "html5lib")

    cont = page_soup.select_one("a.post-thumbnail")

    for link in page_soup.findAll('a', attrs={"class": "post-thumbnail"}):
        urls.append(link.get('href'))

    agami = page_soup.select_one(".nav-links .next")
    # print(agami)
    if agami:
        crawl(page + 1, msl)

        # print(urls)


def main():
    main_url = "https://einsty.com/hi/"
    page_html = requests.get(main_url).content
    page_soup = soup(page_html, "html5lib")

    sub_url = page_soup.select(".navbar .menu-item.menu-item-type-taxonomy a")
    for link_url in sub_url:
        # print(link_url.get("href"))
        l = link_url.get("href")
        crawl(1, l)

    alld = []
    for my_url in urls:
        page_html = requests.get(my_url).content
        page_soup = soup(page_html, "html5lib")
        # print(page_soup)
        cont = page_soup.select("div.card,.post-content")
        alld.append(cont)
        image = page_soup.select_one("div.card")
        # print(cont)
        [tag.extract() for tag in
         image.select('li.post-author ,div.code-block,.post-comment-count,.post-date,script, noscript, .adsbygoogle')]
        for tag1 in page_soup.select("div.code-block"):
            tag1.decompose()
            # print(tag1)

    # fileName = "link.csv"
    # f = open(fileName,"w")
    # f.write(my_url)
    with open('sample1.html', 'wtml> <head> <meta charset=', encoding="utf-8") as f:
        f.write('<h"UTF-8" /> </head><body>')
        # f.write(article_header)

        f.write(str(alld))
        f.write('</body></html>')


if __name__ == "__main__":
    main()