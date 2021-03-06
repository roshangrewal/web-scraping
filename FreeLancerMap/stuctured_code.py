from bs4 import BeautifulSoup as soup
import requests
import re

link = []

def crawl(page):
    global links
    my_url = 'https://www.freelancermap.com/company-presentation.html?pagenr='+str(page)
    page_html = requests.get(my_url).content
    page_soup = soup(page_html, "html5lib")

    containers = page_soup.findAll("div", {"class": "company-row media"})
    Next = page_soup.select('div#page')
    for container in containers:
        links = ("https://www.freelancermap.com" + (container.a["href"]))
        link.append(links)

    if page<27:
        crawl(page+1)

def data():
    filename = "CompaniesInfo6.csv"
    f = open(filename, "w")
    headers = "Company_Name, Description, location, Contact, Email \n"
    f.write(headers)
    for l in link:
        page_html = requests.get(l).content
        page_soup = soup(page_html, "html5lib")
        company_name = page_soup.select("h1.text_extrabig")
        company_name_get_data = company_name[0].text
        company_description = page_soup.select("h2.text_xlarge")
        company_description_get_data = company_description[0].text
        company_location = page_soup.select("ul.list-unstyled")
        company_location_get_data = company_location[0].text
        company_contact = page_soup.select("ul.companyInfo")
        company_contact_get_data = company_contact[0].text

        company_name_final = ' '.join(company_name_get_data.split())
        company_description_final = ' '.join(company_description_get_data.split())
        company_location_final = ' '.join(company_location_get_data.split())
        company_contact_final = ' '.join(company_contact_get_data.split())

        # words = company_contact_final.split()
        # # print(len(words))
        # if '@' in words[-1]:
        #     email = words[-1]
        #
        # elif '@' in words[-2]:
        #     email = words[-2]

        if len(company_contact_final) > 0:
            words = company_contact_final.split()
            # print(len(words))
            if len(words) >= 2:
                if '@' in words[-1]:
                    email=words[-1]

                elif '@' in words[-2]:
                    email=words[-2]
                else:
                    email="Email Not Found in Contact"
            # if '@' in words[-1] and len(words) >= 2:
            #     email = words[-1]
            #
            # elif '@' in words[-2] and len(words) >= 2:
            #     email = words[-2]
            # elif 'a-z' in words[0]:
            #     email = words[0]
            elif '@' in words[0]:
                email=words[0]
            else :
                email="Email Not Found"
        else:
            email = "Data Not Found"


        # print(email)
        # pieces = email.split('@')
        # print(words[-2])

        # temp = re.findall('\" "+@\S+', company_contact_final)
        # print(temp)

        # atpos = company_contact_final.find('@')
        # # print(atpos)
        # sppos = company_contact_final.find(' ', atpos)
        # # print(sppos)
        # host = company_contact_final[atpos+1: sppos]
        # print(host)

        print(company_name_final.replace(',', '')+ ',' + company_description_final.replace(',', '')+ ',' + company_location_final.replace(',', '')+ ',' + company_contact_final.replace(',', '')+ ' ,' +email + "\n")

        # print(company_name_final.replace(",", "").replace("'", "") + ',' + company_description_final.replace(" ", "").strip() + ',' + ll.replace(" ", "").strip() + ',' + cc.replace(" ", "").replace(" ", "").strip()+',' + company_contact_final.find(' ') + "\n")
        f.write(company_name_final.replace(',', '')+ ',' + company_description_final.replace(',', '')+ ',' + company_location_final.replace(',', '')+ ',' + company_contact_final.replace(',', '')+',' + email + "\n")


def main():
    page = 1
    crawl(page)
    data()

if __name__ == "__main__":
    main()