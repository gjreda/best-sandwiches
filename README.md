Chicago Magazine's 50 Best Sandwiches
=============================

About
-------
[Chicago Magazine](http://www.chicagomag.com) recently released their list of [Chicago's 50 best sandwiches](http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/).  I thought it'd be a good reason to learn a little bit more about the Google Maps API, so I made a map.

Besides, everyone likes a good sandwich, right?

How?
-----
1. Get the data from Chicago Magazine's website using [Python](http://www.python.org/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/). See get_sandwiches.py.
2. Load the data into a Google Drive spreadsheet and fill in any missing gaps (yes, there was some manual work).
3. Geocode the addresses in Google Drive using "=ImportData(CONCATENATE("http://maps.google.com/maps/geo?output=csv&q=", <location cell value>)".  This will return the latitude and longitude of each address (hopefully) in the adjacent cells.
4. Convert the spreadsheet to a Google Fusion Table.  Make it publicly available (at least so that people "with the link" can view it).
5. Use some Javascript and the Google Maps v3 API to make a map.
6. Style the map with the [Google's Styled Map Wizard](http://gmaps-samples-v3.googlecode.com/svn/trunk/styledmaps/wizard/index.html).
