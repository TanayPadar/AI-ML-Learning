#DataFrame

import pandas as pd

info = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(info)
print(df)