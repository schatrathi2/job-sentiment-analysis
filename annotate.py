import pandas as pd
import os

def annotate(df):
    num = 1
    for i, row in df.iterrows():
        os.system("clear")
        print(f"post {num} of {len(df)}")
        print(f"text: {row.text}")

        sentiment = int(input("0: neutral, 1: pos, 2: neg - "))
        sentiment_map = {0: "neutral", 1: "pos", 2: "neg"}
        df.loc[i, "sentiment"] = sentiment_map.get(sentiment)

        num += 1

def main():
    year = 2019
    df = pd.read_csv(f"annotate_data_{year}.csv")
    annotate(df)
    df.to_csv(f"annotated_data_{year}.csv", index=False)

if __name__ == "__main__":
    main()