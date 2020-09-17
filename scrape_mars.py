from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

def init_browser():
    executable_path = {'executable_path': '/usr/local/Caskroom/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape_pages():
    browser = init_browser()

    path = "../12-Web-Scraping-and-Document-Databases/page1.html"

    with open(path, encoding='utf-8') as file:
        page1 = file.read()
    soup = BeautifulSoup(page1, 'html.parser')
    page1_title = soup.title.text
    page1_paragraph = soup.body.p.text
    
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    r = requests.get(url2)
    page2 = r.text
    soup2 = BeautifulSoup(page2, 'lxml')
    links = soup2.find_all('img')

    url_fragment = links[3]["src"]
    page2_img_url = f"https://www.jpl.nasa.gov{url_fragment}"   

    url3 = "https://space-facts.com/mars/"
    tables = pd.read_html(url3)

    site_table = pd.DataFrame(tables[0])
    site_table_html = site_table.to_html().replace('\n', '')
    site_table.to_html('site_table.html')

    hemisphere_imgs = [
        {"title": "Cerberus Hemisphere Enhanced", "url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere Enhanced", "url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere Enhanced", "url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere Enhanced", "url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
    ]



    browser.quit()





