#Stack plot is used to show

import matplotlib.pyplot as plt

Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
organic = [50, 60, 70, 80, 90, 100, 100]
direct = [30, 40, 50, 55, 60, 70, 80]
paid = [20, 25, 30, 35, 40, 50, 60]

#firstly X-axis and every data you want to plot in stack format
plt.stackplot(Days, organic, direct, paid, colors=['red', 'blue', 'green']) 
plt.title('Traffic Source')
plt.xlabel('Days')
plt.ylabel('Traffic')
plt.show()
#plt.savefig('Stack_Plot.png')

