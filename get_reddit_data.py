# imports
import requests
import pandas as pd
import time

# constants
SUBREDDITS = ["jobs", "cscareerquestions", "careerguidance"]
YEARS = range(2019, 2026)
MIN_SCORE = 15
TARGET = 5000
OUTPUT_DIR = "reddit_data"

def fetch_year(subreddit, year, target=TARGET):
    after = f"{year}-01-01"
    before = f"{year+1}-01-01"
    posts = []
    last_after = after

    while len(posts) < target:
        # use arctic_shift
        url = (
            f"https://arctic-shift.photon-reddit.com/api/posts/search"
            f"?subreddit={subreddit}"
            f"&after={last_after}&before={before}"
            f"&sort=asc&limit=100"
            f"&fields=id,title,selftext,score,created_utc,subreddit,num_comments"
        )
        r = requests.get(url, headers={"User-Agent": "sentiment-analysis-research"})
        if r.status_code != 200:
            print(f"  Error {r.status_code}: {r.text[:200]}")
            break
        data = r.json().get("data", [])
        if not data:
            break
        filtered = [p for p in data if p.get("score", 0) >= MIN_SCORE]
        posts.extend(filtered)
        print(f"  Page fetched: {len(data)} posts, {len(filtered)} above score {MIN_SCORE}, total so far: {len(posts)}")
        last_after = pd.Timestamp(data[-1]["created_utc"], unit="s").strftime("%Y-%m-%dT%H:%M:%S")
        time.sleep(3)

    return posts[:target]

for sub in SUBREDDITS:
    for year in YEARS:
        print(f"Fetching r/{sub} - {year}")
        posts = fetch_year(sub, year)
        print(f"  Final: {len(posts)} posts")
        if posts:
            df = pd.DataFrame(posts)
            df["created_at"] = pd.to_datetime(df["created_utc"], unit="s")
            df["year"] = df["created_at"].dt.year
            df["month"] = df["created_at"].dt.month
            df.to_csv(f"{OUTPUT_DIR}/{sub}_{year}.csv", index=False)
            print(f"  Saved to {OUTPUT_DIR}/{sub}_{year}.csv")
        time.sleep(5)