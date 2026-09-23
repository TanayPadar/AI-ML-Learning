#Mainly used to find range / frequenct of data

import matplotlib.pyplot as plt

#Data
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

#Plot
custom_bins = [10,20,30,40,50]
plt.hist(ages, bins=custom_bins, color='skyblue', edgecolor='black') #bins = nom of bars i want to print
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')   #it will tell how many people are in that age group
#plt.savefig('Hist_Age_Distribution.png')
plt.show()

#Y axis will always contain frequency of the data
#that's the reason hist needs only one input data, it will select the frequency and divide into range

#bin's ranges are designed automatically but you can also custom them as bins = [10,20,30,40,50]

#Things to Remember -
#1 - Number of bins should be 5-15 . Less makes leak structure and too much makes data noisy
#2 - Use Histogram only for numerical data. Not categorical like PIE Chart 
