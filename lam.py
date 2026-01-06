import pandas as pd

data = {
    "names":["Andhika", "Wiratmoko", "Dwi", "Nurul", "Syafa"],
    "scoreEnglish":[80, 40, 90, 60, 50],
    "scoreMath":[88, 70, 60, 70, 84],
    "scoreIndo":[70, 80, 90, 60, 50]
}
df = pd.DataFrame(data)
df["status"] = "Failed"
df.loc[df["score"] >= 75, "status"] = "Passed"

print(df)