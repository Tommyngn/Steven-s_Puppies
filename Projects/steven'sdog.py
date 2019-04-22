import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin
import urllib.request
import lxml
import csv
from dog_functions import add_new_puppy
from dog_functions import dog_link
from dog_functions import check_if_puppy_isthere



csv_file=open('Shiba_Inu_Puppies.csv', 'a')
csv_writer=csv.writer(csv_file)

# csv_writer.writerow(['Name','Breed', 'Sex', 'Age', 'Price', 'Location'])


list_of_puppies=[]

url_list=[]

current_url='https://www.puppyfind.com/for_sale/?page=1&breed_id=97&country=248&state=CA&city=&order_by=new&sid=40f1k229npt601pd1s1f636330&back=%2Fbreed%2F%3Fbreed_id%3D97%26back%3D%252Fsearch%252F%253Fsubmit%253D1%2526str%253DShiba%252BInu%2526page%253D1'

response = requests.get(current_url)

soup = BS(response.content, 'lxml')

table=soup.find_all('td')

dog_link(current_url,list_of_puppies,csv_writer,'Shiba_Inu_Puppies.csv')

# csv_file.close()
#
# for f in list_of_puppies:
#     print(f)

for pos1, i in enumerate(table):
    if pos1 == 147:
        for pos2, j in enumerate(i):
            # if pos2==3:
            #     print(j)
            if '<a' in str(j):
                print(j)
                url=str(j).strip('<a href="').split('">')
                # url_link=urljoin('https://www.puppyfind.com/for_sale/?page=1&breed_id=97&country=248&state=CA&city=&order_by=new&sid=40f1k229npt601pd1s1f636330&back=%2Fbreed%2F%3Fbreed_id%3D97%26back%3D%252Fsearch%252F%253Fsubmit%253D1%2526str%253DShiba%252BInu%2526page%253D1',url[0])
                print(url)
                # url_list.append(url)
#
# amount=len(url_list)
#
# for url in url_list:
#     print(url)

# print('https://www.puppyfind.com/for_sale/?page=2&breed_id=97&country=248&state=CA&city=&order_by=new&sid=40f1k229npt601pd1s1f636330&back=%2Fbreed%2F%3Fbreed_id%3D97%26back%3D%252Fsearch%252F%253Fsubmit%253D1%2526str%253DShiba%252BInu%2526page%253D1')

csv_file.close()




