#Concatenate - Stack 2 table one above other or side by side

import pandas as pd

cart_df = pd.DataFrame({
    "Product": ["Laptop", "PC", "Mobile", "Tablet"],
    "Price": [100, 200, 300, 400]
})

order_df = pd.DataFrame({
    "Product": ["Laptop", "PC", "Mobile"],
    "Quantity": [1, 2, 3]
})

#Stacking one above other
stacked_df = pd.concat([cart_df, order_df]) 
print(stacked_df)

#Stacking one side by side
stacked_df2 = pd.concat([cart_df, order_df], axis=1)
print(stacked_df2)

stacked_df_3 = pd.concat( [cart_df, order_df], axis=1, ignore_index=True )
print(stacked_df_3)