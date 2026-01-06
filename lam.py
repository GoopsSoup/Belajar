import pandas as pd

data = {
    "names":["Andhika", "Wiratmoko", "Dwi", "Nurul", "Syafa"],
    "scoreEnglish":[80, 40, 90, 60, 50],
    "scoreMath":[88, 66, 60, 68, 84],
    "scoreIndo":[70, 75, 72, 84, 50]
}
df = pd.DataFrame(data)
df["totalScore"] = df[["scoreEnglish", "scoreMath", "scoreIndo"]].sum(axis="columns")
df["averageScore"] = df["totalScore"] / 3 
df["averageScore"] = df["averageScore"].round(1)
df["status"] = "Failed"
df.loc[df["averageScore"] >= 70, "status"] = "Passed"


print(df)