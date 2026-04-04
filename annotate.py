import pandas as pd
from IPython.display import clear_output

annotate_data_2019 = pd.read_csv("annotate_data_2019.csv")
def annotate(df):
    num = 1
    for i, row in df.iterrows():
        clear_output(wait=False)
        print(f"post {num} of {len(df)}")
        print(f"text: {row.text}")

        sentiment = int(input("1: pos, 2: neg - "))
        sentiment_map = {1: "pos", 2: "neg"}
        df.loc[i, "sentiment"] = sentiment_map.get(sentiment)

        num += 1

annotate(annotate_data_2019)