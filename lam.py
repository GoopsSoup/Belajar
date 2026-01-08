import pandas as pd

data = {
    "names":["Andhika", "Wiratmoko", "Dwi", "Nurul", "Syafa"],
    "scoreEnglish":[80, 40, 90, 60, 50],
    "scoreMath":[88, 66, 60, 68, 84],
    "scoreIndo":[70, 75, 72, 84, 50]
}
df = pd.DataFrame(data)
df["totalScore"] = df[["scoreEnglish", "scoreMath", "scoreIndo"]].sum(axis="columns")

#Averaging score
df["averageScore"] = df["totalScore"] / 3 
df["averageScore"] = df["averageScore"].round(1)

#Student status
df["status"] = "Failed"
df.loc[df["averageScore"] >= 70, "status"] = "Passed"

#Total amount of people that passed and failed
status_count = df["status"].value_counts()
passed_students = df.loc[df["status"] == "Passed"]
failed_students = df.loc[df["status"] != "Passed"]

#Top student
top_student = df.loc[df["averageScore"] == df["averageScore"].max()]
lowest_student = df.loc[df["averageScore"] == df["averageScore"].min()]

#Top 3 student
df_largest = df.nlargest(3, "averageScore")
#rank
df["rank"] = df["averageScore"].rank(method="dense", ascending=False)

#Passed subjects
math_passed = df.loc[(df["status"] == "Passed") & (df["scoreMath"] >= 80)]
english_passed = df.loc[(df["status"] == "Passed") & (df["scoreEnglish"] >= 80)]
indo_passed = df.loc[(df["status"] == "Passed") & (df["scoreIndo"] >= 80)]

passed = df.loc[(df.filter(regex="^score") >= 70).all(axis=1)]

print(passed)