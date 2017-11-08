from bs4 import BeautifulSoup as bs
import requests

#from HW hints: like we did in class set up soup and make the requests to the designated site
#save and parse
resp = requests.get('http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General')
html = resp.content
soup = bs(html, 'html.parser')

table = soup.find('table')


#grab all instances where the class is election_item
row = table.find_all('tr', 'election_item')

#grab list of years from the election data, go through each row
yearsList=[]
for row in rows:
        yearsList.append(row.contents[1].text)

#for list of rows, grab the id for the election year and add them
idsList=[]
for i in range(len(rows)):
    idsList.append((rows[i]['id'][-5:]))

#formatting thanks to stackoverflow:
##https://stackoverflow.com/questions/27663924/printing-2-evenly-populated-lists-side-by-side-evenly
fmt = '{:<8}{:<20}{}'

print(fmt.format('', 'Year', 'ID'))
for i, (years, ids) in enumerate(zip(yearsList, idsList)):
    print(fmt.format(i, years, ids))
