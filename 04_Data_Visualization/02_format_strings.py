#It style the liner, maker and color

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
plt.grid(True)
plt.legend() #printed right top box for labels

#[marker][line][color] . Everyone is optional here
plt.plot(X, Y , "r--") #red dashed line
plt.plot(X2, Y2, color="green", marker="^", linestyle="--") #can define like this seperate too

plt.show()
