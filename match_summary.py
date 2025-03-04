import pandas as pd

def generate_match_summary(filepath):
    df = pd.read_excel(filepath)

    match_date = df["Date"].iloc[0]
    teams = df["Team"].unique()

    team_stats = {team: {"Goals": 0, "Shots": 0} for team in teams}

    for _, row in df.iterrows():
        team_stats[row["Team"]]["Goals"] += row["Goals"]
        team_stats[row["Team"]]["Shots"] += row["Shots"]

    print("\nMatch Summary")
    print(f"Date: {match_date}")
    print(f"{teams[0]} {team_stats[teams[0]]['Goals']} - {team_stats[teams[1]]['Goals']} {teams[1]}")

    print("\nTop Performers:")
    top_performers = df[(df["Goals"] > 0) | (df["Assists"] > 0)].sort_values(by=["Goals", "Assists"], ascending=False)
    for _, row in top_performers.iterrows():
        print(f"- {row['Player']} ({row['Team']}): {row['Goals']} Goals, {row['Assists']} Assists")

    print("\nShots on Target:")
    for team, stats in team_stats.items():
        print(f"{team}: {stats['Shots']} shots")

    print("\nSummary saved.")