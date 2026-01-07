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
df["status"].value_counts()
passed_stundets = df.loc[df["status"] == "Passed"]
failed_students = df.loc[df["status"] != "Passed"]

#Top student
top_student = df.loc[df["averageScore"] == df["averageScore"].max()]
lowest_student = df.loc[df["averageScore"] == df["averageScore"].min()]


print(failed_students)