import pandas
#need to import bc no longer in notebook
import matplotlib.pyplot as plt

filename='data/gapminder_gdp_oceania.csv'

#load data and transpose to country names
#gdp data becomes rows
data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

#create plot
ax = data.plot(title = filename)

#set plot attributes
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Cap")

#set x location and labels
ax.set_xticks(range(len(data.index)))
ax.set_xticklabels(data.index,rotation=45)


plt.show()