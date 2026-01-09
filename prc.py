# Practice here!
import pandas as pd

current_data = {
    "store":["Lambda", "Colin", "AppStore", "Cronk", "TvStore"],
    "item":["Laptop", "Phone", "iPad", "PC", "Tv"],
    "daily_cust":[121, 234, 135, 141, 259]
}

df = pd.DataFrame(current_data)

df["crowd"] = "Quiet"
df.loc[(df["daily_cust"] >= 140), "crowd"] = "Crowded"

# V Customer in total V
total_cust = df["daily_cust"].sum(axis=0)
status = df["crowd"].value_counts()
crowded = df.loc[df["crowd"] == "Crowded"]
quiet = df.loc[df["crowd"] == "Quiet"]

# Top stores
recc_store = df.loc[df["daily_cust"] == df["daily_cust"].max()]
df["rank"] = df["daily_cust"].rank(method="dense", ascending=False)

# Store in order of customer
leaderboard = df.nlargest(len(df["store"]), "daily_cust")


print(df.loc[df["item"] == "Laptop"])