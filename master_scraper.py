import requests
from bs4 import BeautifulSoup as bs
import numpy as np

# Connect to Website----------------------------------------------

url = 'https://www.sports-reference.com/cbb/seasons/2019-ratings.html'

page = requests.get(url)
soup = bs(page.text, 'html.parser')
print()

# Get Table-------------------------------------------------

table = soup.find(class_='table_outer_container')

# Get Head--------------------------------------------------

thead = table.find('thead')
th_head = thead.find_all('th')

print('Table Headers:'+'\n')

for thh in th_head:
    headers = [thh.get('data-set')]
    #Get case value
    #table_head = (thh.get_text())
    # Get data-stat value
    #data_stat = thh.get('data-stat')

# Get Body-----------------------------------------------------

tbody = table.find('tbody')
tr_body = tbody.find_all('tr')

schools = ['']

for tr in tr_body:
      # Get id
      
      schools.append(tr.get_text())
      
      # Get data
      th = tr.find('th')
      print(th.get_text())
  
      for td in tr.find_all('td'):
          # Get case value
          print(td.get_text())
          attr = td.get_text()   
          # Get data-stat value
          
          
  