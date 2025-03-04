import pandas as pd
import os

SEASON_STATS_FILE = "data/season_stats.xlsx"

def update_season_stats(match_file):
    match_df = pd.read_excel(match_file)

    if os.path.exists(SEASON_STATS_FILE):
        season_df = pd.read_excel(SEASON_STATS_FILE)
    else:
        season_df = pd.DataFrame(columns=match_df.columns)

    season_df = pd.concat([season_df, match_df], ignore_index=True)
    season_df.to_excel(SEASON_STATS_FILE, index=False)
    print(f"Season stats updated in {SEASON_STATS_FILE}")