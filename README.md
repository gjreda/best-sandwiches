Chicago Magazine's 50 Best Sandwiches
=============================

About
-------
[Chicago Magazine](http://www.chicagomag.com) released their list of [Chicago's 50 best sandwiches](http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/).  I thought it'd be a good reason to learn a little bit more about the Google Maps API, so I made a map (albeit pretty quickly).  The map can be seen [here](http://www.gregreda.com/2013/05/06/more-web-scraping-with-python/).

How?
-----
1. Get the data from Chicago Magazine's website using [Python](http://www.python.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/). See get_sandwiches.py.
2. Clean up data inconsistencies manually.
3. Hit the Google Geocoder API using geocoder.py.
4. Load the data into a publicly accessible Google Fusion Table.
5. Use some Javascript and the Google Maps v3 API to make a map.
6. Style the map with the [Google's Styled Map Wizard](http://gmaps-samples-v3.googlecode.com/svn/trunk/styledmaps/wizard/index.html).

Notes
--------
For those interested, I wrote a [detailed post](http://www.gregreda.com/2013/04/29/more-web-scraping-with-python/) on my blog about the process.
