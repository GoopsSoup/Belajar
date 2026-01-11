# Practice here!
import pandas as pd

current_data = {
    "store":["Lambda", "Colin", "AppStore", "Cronk", "TvStore"],
    "item":["Laptop", "Phone", "iPad", "PC", "Tv"],
    "daily_cust":[121, 234, 135, 141, 259],
    "weekly_cust":[801, 1203, 902, 1002, 1409],
    "monthly_cust":[20000, 12323, 21322, 21311, 20312]
}

df = pd.DataFrame(current_data)

print(df[["weekly_cust", "daily_cust", "monthly_cust"]].sum(axis=1))