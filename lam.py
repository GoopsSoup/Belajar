import pandas as pd

data = {
    "name":["Andhika", "Dwi", "Wiratmoko", "Raja", "Agung"],
    "score":[80, 40, 90, 60, 50]
}
df = pd.DataFrame(data)

print(df[~(df["score"] >= 75)])