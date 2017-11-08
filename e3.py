import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
%matplotlib inline

#get years - make the cs
dataframe = []

#formatting for all years loop
all_years = ['2012', '2008', '2004', '2000', '1996', '1992', '1988', '1984', '1980', '1976', '1972', '1968', '1964', '1960', '1956', '1952', '1948', '1944', '1940', '1936', '1932', '1928', '1924']
for y in range(0, len(all_years)):
    csvv = all_years[y] + ".csv"
    header = pd.read_csv(csvv, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df2 = pd.read_csv(csvv, index_col = 0, thousands = ",", skiprows = [1])

#from hint
    df2.rename(inplace = True, columns = d) # rename to democrat/republican
    df2.dropna(inplace = True, axis = 1)    # drop empty columns
    df2["Year"] = all_years[y]
    df1 = df2[["Republican", "Democratic", "Total Votes Cast", "Year"]]
    dataframe.append(df1.head(4))

finalfile = pd.concat(dataframe)

#create new column with republican share
finalfile["Rep_share"] = finalfile["Republican"]/finalfile["Total Votes Cast"]
finalfile.sort_index()

#create subplots of all the counties/cities
fig, ax = plt.subplots()
finalfile.loc[:,['Year','Rep_share']]
finalfile.reset_index().groupby('County/City').plot(x='Year', y='Rep_share', ax=ax)
plt.show()
