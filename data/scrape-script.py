import urllib2
url = "https://www.petcarerx.com/article/lifespan-of-a-dog-a-dog-years-chart-by-breed/1223"

page = urllib2.urlopen(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

# print soup.prettify().encode('utf-8')

all_tables=soup.find('table', {"class": ' table-responsive'})

print all_tables

data=[]

rows = all_tables.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

# print data

a=[]
b=[]

csv = []

for x in data:
    csv.append(",".join([x[0], x[1]]))
    # a.append(x[0])
    # a.append(x[1])

print "\n".join(csv)

# print a
# print ",".join(a)
# print a
# print b
#
# import pandas as pd
#
# df=pd.DataFrame(a,columns=['breed'])
# df['life']=b
# df
