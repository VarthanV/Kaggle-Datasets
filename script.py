from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from pprint import pprint
import csv


def normalize_data(string: str) -> str:
    if not string:
        return 'NaN'
    if '\n' in string:
        string.replace('\n', '').strip()
        string.replace(',','')


    return string.strip()


URL = 'https://en.wikipedia.org/wiki/List_of_buses'
driver = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver')
driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'lxml')
table_div = soup.find_all(
    'table', {'class': "wikitable sortable jquery-tablesorter"})
print(len(table_div))
csv_file = open('bus.csv', 'a')
fieldnames = ['Name','Type', 'Manufacturer', 'Year', 'Notes', 'Country']
csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
csv_writer.writeheader()
try :
    for i in range(len(table_div)):
        print(i)
        rows = table_div[i].find_all('tr')[1:]
        for row  in rows:
            td = row.find_all('td')
            name = normalize_data(td[0].text)
            type_= normalize_data(td[2].text)
            manufacturer = normalize_data(td[3].text)
            year  = normalize_data(td[4].text)
            notes = normalize_data(td[5].text)
            country =normalize_data(td[6].text)
            csv_writer.writerow({"Name":name,"Type":type_,"Manufacturer":manufacturer,"Year":year,"Notes":notes,"Country":country})
except Exception as e:
    print(e)          

    

    
    # try:
    #     name = normalize_data(td[0].text.strip())
    #     type_ = normalize_data(td[2].text.strip())
    #     manufacturer = normalize_data(td[3].text.strip())
    #     year = normalize_data(td[4].text.strip())
    #     notes = normalize_data(td[5].text.strip())
    #     country = normalize_data(td[6].text.strip())

    #     dictobj = {
    #         "Name": name,
    #         "Type": type_,
    #         "Manufacturer": manufacturer,
    #         "Year": year,
    #         "Notes": notes,
    #         "Country": country
    #     }
    #     csv_writer.writerow(dictobj)
    # except Exception as  e:
    #     print(e)    

    
# for div in table_div:
#     body = div.find('tbody')
#     td = body.find_all('td')
#   
#     except Exception as e:
#         print(e)
