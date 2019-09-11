import requests
from bs4 import BeautifulSoup as BS
import lxml
import csv
from dog_id_functions import get_ID

url='https://www.puppyfind.com/for_sale/?page=1&breed_id=120&country=248&state=CA&city=&order_by=new&sid=vcuqdv7sfi9l4fifqt5hn6v4a4&back=/breed/?breed_id=9&back=/search/?submit=1&str=Shiba%20Inu&page=1'
url_p1='https://www.puppyfind.com/for_sale/?page=1&breed_id='
url_p2='&country=248&state=CA&city=&order_by=new&sid=vcuqdv7sfi9l4fifqt5hn6v4a4&back=/breed/?breed_id=9&back=/search/?submit=1&str=Shiba%20Inu&page=1'

count=1

csv_file=open('Dog_ID.csv','a')
csv_writer=csv.writer(csv_file)

# csv_writer.writerow(['Dog','Dog ID'])

full_url=url_p1+str(count)+url_p2

response=requests.get(full_url)

soup=BS(response.content,'lxml')

# get_ID(csv_writer,soup, count)

# print(len(str(response.content)))


while(len(str(response.content))) != 3:

    get_ID(csv_writer, soup, count)


    count+=1

    response=requests.get(url_p1+str(count)+url_p2)

    soup=BS(response.content,'lxml')




# match=soup.find_all('img')

# for pos1 , i in enumerate(match):
#     if pos1==3:
#         dog_name=str(i).strip('<img alt="').split('" h')
#         dog_name=dog_name[0].split('puppies')
#         print(dog_name[0])









