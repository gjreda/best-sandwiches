from urllib2 import urlopen
import csv
import json
from time import sleep

def geocode(address):
    url = ("http://maps.googleapis.com/maps/api/geocode/json?"
        "sensor=false&address={0}".format(address.replace(" ", "+")))
    return json.loads(urlopen(url).read())

with open("data/best-sandwiches.tsv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")

    with open("data/best-sandwiches-geocode.tsv", "w") as w:
        fields = ["rank", "sandwich", "restaurant", "description", "price",
                 "address", "city", "phone", "website", "full_address",
                 "formatted_address", "lat", "lng"]
        writer = csv.DictWriter(w, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        
        for line in reader:
            print "Geocoding: {0}".format(line["full_address"])
            response = geocode(line["full_address"])
            if response["status"] == u"OK":
                results = response.get("results")[0]
                line["formatted_address"] = results["formatted_address"]
                line["lat"] = results["geometry"]["location"]["lat"]
                line["lng"] = results["geometry"]["location"]["lng"]
            else:
                line["formatted_address"] = ""
                line["lat"] = ""
                line["lng"] = ""
            sleep(1)
            writer.writerow(line)

print "Done writing file"