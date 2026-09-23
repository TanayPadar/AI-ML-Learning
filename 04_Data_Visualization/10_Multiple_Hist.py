#Display Multiple Histograms in the same plot

import matplotlib.pyplot as plt

legit_trans = [
    2.99, 5.49, 8.99, 12.50, 14.99, 17.99, 21.99, 24.99, 
    29.99, 34.99, 39.99, 44.99, 49.99, 54.99, 59.99, 64.99, 
    69.99, 74.99, 79.99, 84.99, 89.99, 94.99, 99.99, 104.99,
]

fraud_trans = [
    28.00, 32.00, 36.00, 40.00, 44.00, 48.00, 52.00, 56.00,
    60.00, 65.00, 70.00, 75.00, 80.00, 85.00, 90.00, 95.00,
    100.00, 106.00, 112.00, 118.00, 124.00, 130.00, 136.00, 142.00,
]

#Plot
plt.hist(legit_trans, bins=20, color='green', edgecolor='black', label='Legit Transactions', alpha=0.5)
plt.hist(fraud_trans, bins=20, color='red', edgecolor='black', label='Fraud Transactions', alpha=0.7)
plt.title('Transaction Amount Distribution')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('Multiple_Hist.png')
plt.show()

#as they are overlapping a alot. we can add the aplha value to ntoice diff