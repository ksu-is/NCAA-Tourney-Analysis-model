import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.sports-reference.com/cbb/schools/gonzaga/2019.html'

page = requests.get(url)
soup = bs(page.text, 'html.parser')

# Get Table
table = soup.find(class_='table_outer_container')


#colomn
col = table.find('colgroup')


# Get Head
thead = table.find('thead')
th_head = thead.find_all('th')

print('Table Headers:'+'\n')
for thh in th_head:
      # Get case value
      print(thh.get_text())
      
      # Get data-stat value
      #print(thh.get('data-stat'))
print()


# Get Body
tbody = table.find('tbody')
tr_body = tbody.find_all('tr')

for trb in tr_body:
      # Get id
      print()
      #print(trb.get('id'))
      
      # Get data
      th = trb.find('th')
      print(th.get_text())
      print(th.get('data-stat'))
      
      for td in trb.find_all('td'):
            # Get case value
            print(td.get_text())
            # Get data-stat value
            print(td.get('data-stat'))
            
            
            
            
            
      

            
      



