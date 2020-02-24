
# Mission-to-Mars


## Background

Build a Web Application that scrapes various websites for data related to Mars and displays the information in a single HTML page


## Objectives

### Step 1 - Scraping

#### NASA Mars News

* Scrape the NASA Mars news site and collected the latest news title and paragraph text.

#### JPL Mars Space Images - Featured Image

* Visited the URL for the JPL featured space image
* Made sure to find the image URL to the full size image
* Made sure to save a complete URL string for this image

#### Mars Weather

* Visited and saved the Mars weather Twitter account and scraped the latest Mars Weather Tweet from the page
    * Saved the Tweet text for the weather report 

#### Mars Facts

* Visited the Mars facts webpage and scrape the planet's facts including diameter, mass, etc.
* Used Pandas to convert the data to a HTML table 

#### Mars Hemispheres

* Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres
* Saved both the image URL string for the full resolution hemisphere imageand name

* Saved all the data collected above in a mars_dictionary

### Step 2 - MongoDB and Flask Application

* Used MongoDB with Flask to create a new HTML page that displays all of the information that was scraped from the URLs above
* Converted Jupyter Notebook into a Python Script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python Dictionary containing all of the scraped data
* Created a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function
    * Stored the return value in Mongo as a Python Dictionary
* Created a root route `/` that will query the Mongo database and pass the Mars data into an HTML template to display the data
* Created a template HTML file called `index.html` that will take the Mars data dictionary and display all of the data in the appropriate HTML elements
