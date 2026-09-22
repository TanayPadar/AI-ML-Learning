import matplotlib.pyplot as plt

#mainly used to see co-relation , outliers and clusters

age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
blood_pressure = [110, 115, 120, 125, 130, 135, 140, 145, 120, 155]

plt.scatter(age, blood_pressure, color="red", marker="o" , alpha=0.5, cmap="OrRd") #alpha for transperancy 
plt.title("Age vs Blood Pressure")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.annotate("Outlier", xy=(60, 120), xytext=(61, 121) #text, xy position of dot, xy pos of text)
plt.show()

