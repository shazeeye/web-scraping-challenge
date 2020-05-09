#!/usr/bin/env python
# coding: utf-8

# Dependencies and Setup

from splinter import Browser
import requests as req
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
import pandas as pd


# @NOTE: Replace the path with your actual path to the chromedriver
# open chrome driver browser
def init_browser():
    #executable_path = {"executable_path": "/usr/local/Caskroom/chromedriver/80.0.3987.16/chromedriver"}
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# defining scrape & dictionary
def scrape():
    
    mars_dictionary={}  
    browser = init_browser() 
    # Step 1: Scraping for latest News Article
    # Visit website to scrape Mars mission
    #url = 'https://mars.nasa.gov/news/'
    browser.visit('https://mars.nasa.gov/news/')

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get the news title

    news_title = soup.find('div', class_='content_title').text
    mars_dictionary['news_title']=news_title 

    # Get the paragraph text
    news_p=soup.find('div', class_='rollover_description_inner').text
   
    mars_dictionary['news_paragraph']=news_p


    # Step 1: Scraping Mars Space Images 

    #URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)   
    time.sleep(1)
     # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(10)
    #Clicking on button 'Full Image' to get large image
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    time.sleep(10)
    new_html = browser.html
    new_soup = bs(new_html, 'html.parser')
    temp_img_url = new_soup.find('img', class_='main_image')
    back_half_img_url = temp_img_url.get('src')

    image_url = "https://www.jpl.nasa.gov" + back_half_img_url
   
    mars_dictionary['featured_image']=image_url


  


    #Step 1: Scraping Mars weather from Twitter
    #URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    #Pulling in data using this text as the other says Chrome not accessible
    driver = webdriver.Chrome()
    driver.get(url)
    html=req.get(url)
    #html = browser.html


    # Create BeautifulSoup object
    soup = bs(html.text, 'html.parser')
    #soup = bs(html, 'lxml')

    #Tweet text
    tweets = soup.find('ol', class_='stream-items')
    mars_weather = tweets.find('p', class_="tweet-text").text
    #mars_weather = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").find('span').text

    mars_dictionary['mars_weather']=mars_weather  




    # Step 1: Scraping Mars Facts
    mars_facts_url = "https://space-facts.com/mars/"

    # read html into pandas
    tables = pd.read_html(mars_facts_url)

    # It returns 3 tables. The first has the data needed.

    df = tables[0]
    df.columns = ["Description", "Value"]

   

    # convert to html table

    mars_facts_html=df.to_html(index=False)

    mars_facts_html

    mars_dictionary['mars_facts_html']=mars_facts_html
    # Step 1: Scraping Mars hemispheres




    # define url and open in browser
    hemisphere_img_urls = []
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)


    # Getting Cerberus image link and title

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Cerberus')


    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    cerberus_soup = bs(hemispheres_html, 'html.parser')

    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    cerberus_url = hem_base_url + cerberus_img
    #hemisphere_img_urls.append(cerberus_url)
    mars_dictionary['cerberus_url']=cerberus_url 
    # Getting Schiaparelli image link and title

    # click on the link for the Schiaparelli hemisphere
    browser.click_link_by_partial_text('Schiaparelli')
    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    schiaparelli_soup = bs(hemispheres_html, 'html.parser')

    schiaparelli = schiaparelli_soup.body.find('img', class_ = 'wide-image')
    schiaparelli_img = schiaparelli['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    schiaparelli_url = hem_base_url + schiaparelli_img
    #hemisphere_img_urls.append(schiaparelli_url)
    mars_dictionary['schiaparelli_url']=schiaparelli_url

    # Getting Syrtis image link and title
    # click on the link for the Syrtis hemisphere
    browser.click_link_by_partial_text('Syrtis')
    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    syrtis_soup = bs(hemispheres_html, 'html.parser')

    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = schiaparelli['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    syrtis_url = hem_base_url + syrtis_img
    #hemisphere_img_urls.append(syrtis_url)
    mars_dictionary['syrtis_url']=syrtis_url


    # Getting Valles image link and title
    # click on the link for the Valles hemisphere
    browser.click_link_by_partial_text('Valles')
    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    valles_soup = bs(hemispheres_html, 'html.parser')

    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    valles_url = hem_base_url + valles_img
    #hemisphere_img_urls.append(valles_url)
    mars_dictionary['valles_url']=valles_url

    #mars_dictionary["hemisphere_img_url"] = hemisphere_img_urls
    print(mars_dictionary)
    return mars_dictionary

    browser.quit()



