#Merging two tables into single like for Online Shopping Cart

import pandas as pd

cart_df = pd.DataFrame({
    "Product": ["Laptop", "PC", "Mobile", "Tablet"],
    "Price": [100, 200, 300, 400]
})
print(cart_df)

order_df = pd.DataFrame({
    "Product": ["Laptop", "PC", "Mobile"],
    "Quantity": [1, 2, 3]
})
print(order_df)

merged_df = pd.merge(cart_df, order_df, on="Product", how="left") #on = What to merge on. Bcz Product is common in both tables.
print(merged_df)
#This will merge the two tables into a single table
#Merged will skip the unmatched rows like Tablet.

#Inner Join (by default) - Merges only Matched data
#Left Join - Merges all rows from the left table and the matched rows from the right table. Gives Nan when no info in right table
#Right Join - Merges all rows from the right table and the matched rows from the left table. Gives Nan when no info in left table
#Outer Join - Merges all rows from both tables and the matched rows from both tables. Gives Nan when no info in either table


