from bs4 import BeautifulSoup as bs
import requests

#from HW hints: like we did in class set up soup and make the requests to the designated site
#save and parse
resp = requests.get('http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General')
html = resp.content
soup = bs(html, 'html.parser')


table = soup.find('table')

#grab all instances where the class is election_item
rows = table.find_all('tr', 'election_item')

#grab list of years from the election data, go through each row
yearsList=[]
for row in rows:
        yearsList.append(row.contents[1].text)

#for list of rows, grab the id for the election year and add them
idsList=[]
for i in range(len(rows)):
    idsList.append((rows[i]['id'][-5:]))



#base that will be formatted
base = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

q2 = dict(zip(idsList, yearsList))

#Write a loop that basically downloads all of the csv files
#by visiting each of the ID-specific links and writing their content to a separate csv.

for id in idsList:
    lastyear_url = base.format(id)
    lastyear_text = requests.get(lastyear_url).text
    ElecYearData = q2[id] + ".csv"

    with open(ElecYearData, 'w') as output:
        output.write(lastyear_text)
