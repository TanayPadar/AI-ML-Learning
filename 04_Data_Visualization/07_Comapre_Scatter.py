#Compare data in Scatter

import matplotlib.pyplot as plt
import numpy as np

#Winter Temp vs Humidity
winter_temp = [5, 2, 10, 0,7]
winter_humidity = [80, 75, 65, 85, 70]

#Summer Temp vs Humidity
summer_temp = [25, 30, 28, 35, 27]
summer_humidity = [60, 50, 55, 45, 65]

plt.scatter(winter_temp, winter_humidity, color='red', label='Winter')
plt.scatter(summer_temp, summer_humidity, color='blue', label='Summer')
plt.legend()

#Add title and labels
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.savefig('Temperature_vs_Humidity_scatter.png')
plt.show()