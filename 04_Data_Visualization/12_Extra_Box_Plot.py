#2 sets on same chart

import matplotlib.pyplot as plt

#Data
data1 = [7, 8, 5, 6, 9, 4, 10, 12, 15, 50]
data2 = [18, 20, 21, 22, 24, 25, 27, 28, 30, 32]

#Plot
plt.boxplot(data1, positions=[1])
plt.boxplot(data2, positions=[2])
plt.xticks([1, 2], ['data1', 'data2'])
plt.grid(True)
plt.show()
#plt.savefig('Extra_Box_Plot.png')

