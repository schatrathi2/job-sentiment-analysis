import pandas as pd
from IPython.display import clear_output

year = 2019
df = pd.read_csv(f"annotate_data_{year}.csv")
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
df.to_csv(f"annotated_data_{year}.csv", index=False)