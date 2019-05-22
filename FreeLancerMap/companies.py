from bs4 import BeautifulSoup as soup
import requests
import pandas as pd

link = []
# lst1 = []
# lst2 = []
# lst3 = []
# lst4 = []


def crawl(page):
    global links
    my_url = 'https://www.freelancermap.com/company-presentation.html?pagenr='+str(page)
    # print(my_url)
    page_html = requests.get(my_url).content
    page_soup = soup(page_html, "html5lib")

    containers = page_soup.findAll("div", {"class": "company-row media"})
    # print(len(containers))
    Next = page_soup.select('div#page')
    for container in containers:
        links = ("https://www.freelancermap.com" + (container.a["href"]))
        link.append(links)
        # print("Link:" + links)
        # print(link)

    if page<2:
        crawl(page+1)



def data():
    global h,d,lo,c
    for l in link:

        page_html = requests.get(l).content
        page_soup = soup(page_html, "html5lib")
        heading = page_soup.select("h1.text_extrabig")
        h = heading[0].text

        # lst1.append(h)
        desc = page_soup.select("h2.text_xlarge")
        d = desc[0].text
        # lst2.append(d)
        loc = page_soup.select("ul.list-unstyled")
        lo = loc[0].text
        # lst3.append(lo)
        con = page_soup.select("ul.companyInfo")
        c = con[0].text


        # lst4.append(c)
        # print(str(c.split()))
        # print(c.strip())
        # print(c.split('\n').removeAll(','))

        # email = page_soup.select("i.fa-envelope")
        # e = email[0].text
        # web = page_soup.select("i.fa-globe")
        # w = web[0].text

        print(h,d,lo,c)
        # print(page_soup)
        # print("links array: " + l)




def main():

    page = 1
    crawl(page)
    data()
    # print(lst1)
    # print(lst2)
    # print(lst3)
    # print(lst4)
    # with open('sample.html', 'w', encoding="utf-8") as f:
    #     f.write('<html> <head> <meta charset="UTF-8" /> </head><body>')
    #     # f.write(article_header)
    #
    #
    #     f.write(str(lst1))
    #     f.write(str(lst2))
    #     f.write(str(lst3))
    #     f.write(str(lst4))
    #
    #     f.write('</body></html>')
    #     f.close()

    # filename = "CompaniesInformation3.csv"
    # f = open(filename, "w")
    # headers = "Company_Name, Description, location, Contact, Email, Website \n"
    # f.write(headers)
    # f.write(lst1 + lst2 + lst3 + "\n")
    # f.close()



if __name__ == "__main__":
    main()