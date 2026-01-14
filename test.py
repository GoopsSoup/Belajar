import pandas as pd

df = pd.DataFrame({
    "math": [80, 60, 90],
    "english": [70, 85, 50]
})


print(df[["math", "english"]].ge(70).all(axis=1))
# anjat