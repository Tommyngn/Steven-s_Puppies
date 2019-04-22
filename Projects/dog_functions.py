import requests
from bs4 import BeautifulSoup as BS
import lxml
import csv


def add_new_puppy(name,breed, sex, age, price, location, list_,csv_):
    dict_={'Name': name, 'Breed': breed, "Sex": sex, 'Age': age,'Price': price, 'Location': location}

    list_.append(dict_)

    csv_.writerow([name,breed, sex, age, price, location])


def check_if_puppy_isthere(name, list_,csv_file):
    # for i in list_:
    #     dict_=i
    #     if name in dict_['Name']:
    #         return True
    #
    # return False

    with open(csv_file, 'r') as f:
        read=f.readlines()
        for x in read:
            list_=x
            list_=list_.split(',')
            if name in list_[0]:
                return True

    return False

def dog_link(url, list_of_puppies,csv_,csv_file):
    url = url
    response = requests.get(url)

    soup = BS(response.content, 'lxml')

    main_table = soup.find_all("tr")

    count = 0
    spot = 5
    spot2 = 5

    for pos, i in enumerate(main_table):
        # print('POSITION' + str(pos) + '::' , i)

        if pos % spot2 == 0:
            if pos == 55:
                spot = 56
                # print(spot)
                spot2 = 2
                # print(spot2)
            elif pos == spot:
                count = pos
                for pos2, j in enumerate(i):
                    # print('POSITIONghhghghghghg'+str(pos2),j)
                    if 'title="Shiba Inu Puppy for Sale..."><b>' in str(j):
                        str_ = str(j).split('><b>')
                        name_ = str_[1]
                        name_list = name_.split('</b>')
                        full_name = name_list[0]
                        # print(full_name)

                for pos2, j in enumerate(i):
                    if pos2 == 5:
                        list_ = str(j).split('</tr>')
                        for pos3, k in enumerate(list_):
                            if pos3 > 1 and pos3 < 7:
                                if pos3 == 2:
                                    temp_list = str(k).split('>')
                                    breed = temp_list[2].strip('Breed:  ').strip('</td')
                                    # print(breed)
                                elif pos3 == 3:
                                    temp_list = str(k).split('>')
                                    sex = temp_list[2].strip('Sex:  ').strip('</td')
                                    # print(sex)
                                elif pos3 == 4:
                                    temp_list = str(k).split('>')
                                    age = temp_list[2].strip('age:  ').strip('</td')
                                    # print(age)
                                elif pos3 == 5:
                                    temp_list = str(k).split('>')
                                    price = temp_list[2].strip('Price:  ').strip('</td')
                                    # print(price)
                                elif pos3 == 6:
                                    temp_list = str(k).split('>')
                                    location = temp_list[2].strip('Location:  ').strip('</td')
                                    # print(location)

                if sex == 'Male':
                    if check_if_puppy_isthere(full_name, list_of_puppies,csv_file) == False:
                        add_new_puppy(full_name, breed, sex, age, price, location, list_of_puppies,csv_)
                        print(full_name)

            elif pos == (count + 10):
                count = pos

                for pos2, j in enumerate(i):
                    # print('POSITIONghhghghghghg'+str(pos2),j)
                    if 'title="Shiba Inu Puppy for Sale..."><b>' in str(j):
                        str_ = str(j).split('><b>')
                        name_ = str_[1]
                        name_list = name_.split('</b>')
                        full_name = name_list[0]
                        # print(full_name)

                for pos2, j in enumerate(i):
                    if pos2 == 5:
                        list_ = str(j).split('</tr>')
                        for pos3, k in enumerate(list_):
                            if pos3 > 1 and pos3 < 7:
                                if pos3 == 2:
                                    temp_list = str(k).split('>')
                                    breed = temp_list[2].strip('Breed:  ').strip('</td')
                                    # print(breed)
                                elif pos3 == 3:
                                    temp_list = str(k).split('>')
                                    sex = temp_list[2].strip('Sex:  ').strip('</td')
                                    # print(sex)
                                elif pos3 == 4:
                                    temp_list = str(k).split('>')
                                    age = temp_list[2].strip('age:  ').strip('</td')
                                    # print(age)
                                elif pos3 == 5:
                                    temp_list = str(k).split('>')
                                    price = temp_list[2].strip('Price:  ').strip('</td')
                                    # print(price)
                                elif pos3 == 6:
                                    temp_list = str(k).split('>')
                                    location = temp_list[2].strip('Location:  ').strip('</td')
                                    # print(location)

                if sex == 'Male':
                    if check_if_puppy_isthere(full_name, list_of_puppies,csv_file) == False:
                        add_new_puppy(full_name, breed, sex, age, price, location, list_of_puppies,csv_)
                        print(full_name)
