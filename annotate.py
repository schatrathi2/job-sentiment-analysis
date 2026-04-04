import pandas as pd
from IPython.display import clear_output

df = pd.read_csv("annotate_data_2019.csv")
def annotate(df):
    num = 1
    for i, row in df.iterrows():
        clear_output(wait=False)
        print(f"post {num} of {len(df)}")
        print(f"text: {row.text}")

        sentiment = int(input("0: neutral, 1: pos, 2: neg - "))
        sentiment_map = {0: "neutral", 1: "pos", 2: "neg"}
        df.loc[i, "sentiment"] = sentiment_map.get(sentiment)

        num += 1

annotate(df)
df.to_csv("annotated_data_2019.csv", index=False)