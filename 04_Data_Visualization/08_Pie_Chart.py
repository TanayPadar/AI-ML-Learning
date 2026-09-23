#Used for Relative data like market share of iphone and Samsung = 100%


import matplotlib.pyplot as plt

#Data
iphone_market_share = 45
samsung_market_share = 35
other_market_share = 20

#Plot
plt.pie([iphone_market_share, samsung_market_share, other_market_share], labels=['iPhone', 'Samsung', 'Other'], 
autopct='%1.1f%%',#autopct for percentage display
    wedgeprops={'linewidth': 1, 'edgecolor': 'black'},#border color of each slice
    explode=(0, 0, 0.1), shadow=True, #explode the other_market_share BY 10%
    ) #autopct for percentage display
plt.title('Market Share of iPhone and Samsung')
#plt.savefig('Market_Share_of_iPhone_and_Samsung.png')
plt.show()