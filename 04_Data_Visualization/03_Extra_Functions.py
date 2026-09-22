#Extra functions for styling

import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]
X2 = [1,3,6,6,5]
Y2 = [1,5,11,14,17]

plt.plot(X, Y , label="First Line")
plt.plot(X2, Y2, label="Second Line") #line chart by default
plt.title("Square of Numbers")
plt.xlabel("Numbers")
plt.ylabel("Squares")
plt.legend() #printed right top box for labels

#Extra Styling Functions
print (plt.style.available) #to see all the styles available
plt.style.use("dark_background") #selected style from aviable
plt.grid(True) #grid on by default
plt.savefig("matplotlib_intro.png") #save the figure as a png file

#to increase the size of the chart size
plt.ylim(0, max(Y2)+5) #will increase height by Y2's max value +5


plt.plot #for line chat
plt.bar #for bar chart
plt.barh #for horizontal bar chart
plt.pie #for pie chart
plt.scatter #for scatter plot
plt.hist #for histogram
plt.boxplot #for box plot
plt.show()
