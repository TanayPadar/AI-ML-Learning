import matplotlib.pyplot as plt
import numpy as np

oscar_movies = ["The revenant", "Birdman", "12 years a slave", "Argo", "The hurt locker"]
oscar_revenue = [1005, 170, 427, 133, 232] #in $Million

non_oscar_movies = ["Avatar", "Titanic", "The Lord of the Rings", "The Dark Knight", "Fight Club"]
non_oscar_revenue = [2787, 2187, 2912, 2615, 408] #in $Million

years = [2010, 2009, 2008, 2007, 2006]

plt.title("Oscar vs Non-Oscar Movies Revenue")
plt.xlabel("Years")
plt.ylabel("Revenue (in $M)")

width = 0.4
x = np.arange(len(years))  # positions: 0, 1, 2, 3, 4

plt.bar(x - width / 2, oscar_revenue, width, label="Oscar")
plt.bar(x + width / 2, non_oscar_revenue, width, label="Non-Oscar")

plt.xticks(x, years)  # year label under each pair
plt.legend()

plt.show()