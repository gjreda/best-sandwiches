#!/usr/bin/python
# Greg Reda
# 2012.10.14
# Get Chicago Magazine's list of the 50 best sandwiches in Chicago
# Source: http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/
# Blog: http//www.gregreda.com/2013/04/29/more-web-scraping-with-python/

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

base_url = ("http://www.chicagomag.com/Chicago-Magazine/"
            "November-2012/Best-Sandwiches-Chicago/")

soup = BeautifulSoup(urlopen(base_url).read())
sammies = soup.find_all("div", "sammy")
sammy_urls = [div.a["href"] for div in sammies]

with open("data/src-best-sandwiches.tsv", "w") as f:
    fieldnames = ("rank", "sandwich", "restaurant", "description", "price",
                    "address", "phone", "website")
    output = csv.writer(f, delimiter="\t")
    output.writerow(fieldnames)

    for url in sammy_urls:
        url = url.replace("http://www.chicagomag.com", "")  # inconsistent URL
        page = urlopen("http://www.chicagomag.com{0}".format(url))
        soup = BeautifulSoup(page.read()).find("div", {"id": "sandwich"})
        rank = soup.find("div", {"id": "sandRank"}).encode_contents().strip()
        sandwich = soup.h1.encode_contents().strip().split("<br />")[0]
        restaurant = soup.h1.span.encode_contents()
        description = soup.p.encode_contents().strip()
        addy = soup.find("p", "addy").em.encode_contents().split(",")[0].strip()
        price = addy.partition(" ")[0].strip()
        address = addy.partition(" ")[2].strip()
        phone = soup.find("p", "addy").em.encode_contents().split(",")[1].strip()
        if soup.find("p", "addy").em.a:
            website = soup.find("p", "addy").em.a.encode_contents()
        else:
            website = ""

        output.writerow([rank, sandwich, restaurant, description, price,
                        address, phone, website])

print "Done writing file"
