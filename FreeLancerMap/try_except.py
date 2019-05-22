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

    if page<2:
        crawl(page+1)

def data():
    # filename = "CompaniesData11.csv"
    # f = open(filename, "w")
    # headers = "Company_Name, Description, location, Contact, Email \n"
    # f.write(headers)
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

        try:
            company_contact_final = ' '.join(company_contact_get_data.split())
            #Code for email extraction
            if len(company_contact_final) > 0:
                words = company_contact_final.split()
                # print(len(words))
                if len(words) >= 2:
                    if '@' in words[-1]:
                        email=words[-1]

                    elif '@' in words[-2]:
                        email=words[-2]
                    else:
                        email="Email Not Found!"
                elif '@' in words[0]:
                    email=words[0]
                else :
                    email="Email Not Found!!"
            else:
                email = None
        except:
            email=None

        #Code for website extraction
        if len(company_contact_final) > 0:
            contact = company_contact_final.split()
            print(type(contact))
            print(len(contact))
            if len(contact) >= 2:
                if 'www' or 'hhtp' in contact[-1]:
                    website=contact[-1]
                    contact.remove(contact[-1])

                elif 'www' or 'http' in contact[-2]:
                    website=contact[-2]
                    contact.remove(contact[-2])
                else:
                    website="Website Not Found!"
            elif 'www' or 'http' in contact[0]:
                website=contact[0]
                contact.remove(contact[0])
            else :
                website="Website Not Found!!"
        else:
            website = None

        print(company_name_final.replace(',', '')+ ',' + company_description_final.replace(',', '')+ ',' + company_location_final.replace(',', '')+ ',' + company_contact_final.replace(',', '')+ ' ,' +email+ ','+ website + "\n")

        # print(company_name_final.replace(",", "").replace("'", "") + ',' + company_description_final.replace(" ", "").strip() + ',' + ll.replace(" ", "").strip() + ',' + cc.replace(" ", "").replace(" ", "").strip()+',' + company_contact_final.find(' ') + "\n")
        # f.write(company_name_final.replace(',', '')+ ',' + company_description_final.replace(',', '')+ ',' + company_location_final.replace(',', '')+ ',' + company_contact_final.replace(',', '')+',' + email + "\n")

def main():
    page = 1
    crawl(page)
    data()

if __name__ == "__main__":
    main()