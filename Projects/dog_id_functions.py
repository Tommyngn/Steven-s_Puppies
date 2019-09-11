import csv
import requests
from bs4 import BeautifulSoup as BS

def get_ID(csv_writer, soup,count):

    match=soup.find_all('img')

    for pos1 , i in enumerate(match):
        if pos1==3:
            dog_name=str(i).strip('<img alt="').split('" h')
            dog_name=dog_name[0].split('puppies')
            csv_writer.writerow([dog_name[0], count])
            print(count)

