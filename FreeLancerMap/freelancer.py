from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.freelancermap.com/it-projects.html'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li", {"class": "project-row"})
# print(len(containers))

# print(soup.prettify(containers[0]))

container=containers[0]
print(container.a["href"])

job_title=container.findAll("h3", {"class": "title"})
print(job_title[0].text)

location=container.findAll("span", {"class": "country"})
print(location[0].text.strip())

job_type=container.findAll("span", {"class": "contract"})
print(job_type[0].text.strip())

company=container.findAll("div", {"class": "company"})
print(company[0].text)

listed=container.findAll("div", {"class": "created"})
print(listed[0].text)

description=container.findAll("p", {"class": "description"})
print(description[0].text)

skills=container.findAll("div", {"class": "categories"})
print(skills[0].text)
'''

filename="JD.csv"
f=open(filename, "w")

headers="job_title, location, job_type, company, listed, description, skills\n"
f.write(headers)

for container in containers:
    job_title_container = container.findAll("h3", {"class": "title"})
    job_title = job_title_container[0].text.strip()

    location_container = container.findAll("span", {"class": "country"})
    location = location_container[0].text.strip()

    job_type_container = container.findAll("span", {"class": "contract"})
    job_type = job_type_container[0].text.strip()

    company_container = container.findAll("div", {"class": "company"})
    company = company_container[0].text.rstip()

    listed_container = container.findAll("div", {"class": "created"})
    listed = listed_container[0].text.rstip()

    description_container = container.findAll("p", {"class": "description"})
    description = description_container[0].text.rstip()

    skills_container = container.findAll("div", {"class": "categories"})
    skills = skills_container[0].text.rstrip()

    # print("product_name:" + job_title)
    # print("price" + price)
    # print("ratings" + rating)


    #String Parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "RS." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()
'''