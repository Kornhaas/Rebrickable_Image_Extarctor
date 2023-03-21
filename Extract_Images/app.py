import inspect
import pandas as pd
from icecream import ic


# read all HTML tables from specific URL
import requests
from urllib.request import Request, urlopen
import os

CURRENTBASEDIR = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

brickstype = "Plants_and_Animals"

try:
    os.mkdir("d:\lego\\" + brickstype)
    print("Directory is created")
except FileExistsError:
    print("Directory already exists")


lookup = pd.read_csv(CURRENTBASEDIR + "\\lookup.csv")

url = "https://rebrickable.com/parts/?format=table&csrfmiddlewaretoken=EPGKyNnHP6vde32wcYPq9jllJ5ZpFKSLD91T46TOVqfGJfIUK8DGZ5reN8jWbbvk&get_drill_downs=&min_year=1945&max_year=2023&min_part_cost=0&max_part_cost=20&q=&part_cat=28&exists_in_color=&_=1679299582064&csrfmiddlewaretoken=EPGKyNnHP6vde32wcYPq9jllJ5ZpFKSLD91T46TOVqfGJfIUK8DGZ5reN8jWbbvk&get_drill_downs=&min_year=1945&max_year=2023&min_part_cost=0&max_part_cost=20&q=&part_cat=28&exists_in_color=&_=1679299582064"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
# ic(webpage)
df = pd.read_html(webpage)[0]
df.to_csv("d:\lego\\" + brickstype + "\data.csv", index=False)

ic(df)
number = 0 
for ind in df.index:
    number = number + 1
    imagename= str(df['Part Num'][ind])
    try:
        
        mask = lookup.query('part_num ==  @imagename')[['part_num','img_url']]
        url =mask.iloc[:1]
                
        img_data = requests.get(url.iloc[0]['img_url']).content
        with open("d:\lego\\" + brickstype + "\\"+ '{0:04}'.format(number) + "_" +imagename+".jpg", 'wb') as handler:
            handler.write(img_data)
    except:
        print("error: " + '{0:04}'.format(number) + "_"  + str(df['Part Num'][ind]))
