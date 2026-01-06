import pandas as pd

data = {
    "names":["Andhika", "Wiratmoko", "Dwi", "Nurul", "Syafa"],
    "scoreEnglish":[80, 40, 90, 60, 50],
    "scoreMath":[88, 66, 60, 68, 84],
    "scoreIndo":[70, 75, 72, 84, 50]
}
df = pd.DataFrame(data)
df["totalScore"] = df[["scoreEnglish", "scoreMath", "scoreIndo"]].sum(axis="columns")
df["status"] = "Failed"
df["averageScore"] = df["totalScore"] / len(df["scoreEnglish"])
df.loc 


print(df)