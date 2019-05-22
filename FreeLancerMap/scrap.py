from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.freelancermap.com/it-projects/projects/it/1770521-projekt-azure-architect-amsterdam.html'



url = requests.get(my_url).content

page_soup = soup(url, "html.parser")

cont = page_soup.select("top_seo")

# for a in cont:
#     print(a)

# print(soup.prettify(containers[0]))

container=containers[0]
print(container.div.img["alt"])

price=container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings=container.findAll("div", {"class": "niH0FQ"})
#print(ratings[0].text)

filename="product_details.csv"
f=open(filename, "w")

headers="Product_Name, Pricing, Rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "niH0FQ"})
    rating=rating_container[0].text

    #print("product_name:" + product_name)
    #print("price" + price)
    #print("ratings" + rating)


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
