import matplotlib.pyplot as plt

years = [2008, 2009, 2010, 2011, 2012]
oscarrevenue = [1005, 170, 427, 133, 232] #in $Million
plt.bar(years, oscarrevenue)
plt.title("Oscar Revenue")
plt.xlabel("Years")
plt.ylabel("Revenue (in $M)")

#plt.text to add label to each bar. [x axis, y axis, text, alignment]
plt.text(years[0] +10, oscarrevenue[0], "Text" , ha="center") #+10 to add gap from the bar

plt.show()