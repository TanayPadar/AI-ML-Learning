#It summarizes the data into 5 key values
#1 - Minimum
#2 - First Quartile (25% of data)
#3 - Median (50% of data)
#4 - Third Quartile (75% of data)
#5 - Maximum

#How it works ?
#1 - Sort the data like - 4,5,6,7,8,9,10,12,15
#2 - The median is 8 (50% of data)
#3 - The first quartile is 6 (25% of data)
#4 - The third quartile is 10 (75% of data)
#5 - The minimum = Q1 - 1.5 * (Q3 - Q1)    == 0
#6 - The maximum = Q3 + 1.5 * (Q3 - Q1)   ==16
#7 - But these max & min value are not exactly marked on chart. Marked value is found in range btwn given data. Like 2 for min and 15 for max

#The yellow in middle is the median
#The upper line of box is Q3
#The lower line of box is Q1
#The top line is range that upper whisker/outlier is outside of this range
#The bottom line is range that lower whisker/outlier is outside of this range
import matplotlib.pyplot as plt

#Data      
data = [7, 8, 5, 6, 9, 4, 10, 12, 15]

#Plot
plt.boxplot(data)
plt.grid(True)
plt.show()
#plt.savefig('Box_Plot.png')

#If i add 50 to range of data, the outlier 50 will marked as DOT on map

