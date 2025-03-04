from data_entry import collect_match_data
from match_summary import generate_match_summary
from stats_tracker import update_season_stats

def main():
    print("Big Sky Women's Soccer - Match Data Entry")
    match_data_file = collect_match_data()
    generate_match_summary(match_data_file)
    update_season_stats(match_data_file)
    print("All done! Data saved and season stats updated.")

if __name__ == "__main__":
    main()