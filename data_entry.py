import pandas as pd
from datetime import datetime
import os

def collect_match_data():
    match_date = input("Match Date (YYYY-MM-DD): ")
    team_a = input("Team A Name: ")
    team_b = input("Team B Name: ")

    players = []
    for team in [team_a, team_b]:
        print(f"Enter players for {team} (comma separated):")
        player_list = input().split(",")
        players.extend([(team, player.strip()) for player in player_list])

    data = []
    for team, player in players:
        print(f"Enter stats for {player} ({team}):")
        goals = int(input("Goals: "))
        assists = int(input("Assists: "))
        shots = int(input("Shots: "))
        passes = int(input("Passes: "))
        data.append([match_date, team, player, goals, assists, shots, passes])

    df = pd.DataFrame(data, columns=["Date", "Team", "Player", "Goals", "Assists", "Shots", "Passes"])

    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/match_data_{match_date}_{team_a}_vs_{team_b}.xlsx"
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")
    return filename