import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import json

driver = webdriver.Chrome("/Users/roliasong/Desktop/LING/chromedriver")

url = "https://ic.byu.edu/archives/" #hard-coded starting url
driver.get(url)

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"} #user-agent
response = requests.get(url, headers=headers)
soup = bs(response.content, "html.parser")

# driver.find_element_by_xpath("//a[@href='#tab-1534298677995-0-10']").click()
anchors = soup.find_all("a") #creates a bs4 list thing that contains all the "a" elements on the url page
temp = [] #creates an empty dictionary for the href links in each a tag
links = []

for anchor in anchors: #for each a tag in the list
    try:
        temp.append(anchor.attrs['href']) #if it has a href attribute, add it to links
    except KeyError:
        print("skipping this anchor because it doesn't have an href attribute") #if no href attribute, print this statement

temp = [t for t in temp if t[0] != "#"] #gets rid of same page links
temp = [t for t in temp if len(t) > 20]
for t in temp:
    if t[19] == "s" and t[20] == "e":
        links.append(t)
#the above for loop includes the winter, spring/summer, and fall links. Those ones I'm just removing manually

with open("/Users/roliasong/Desktop/Dintern/from_geospatial/posters" + ".json", "w") as outfile:
    outfile.write(json.dumps(links, ensure_ascii=False))