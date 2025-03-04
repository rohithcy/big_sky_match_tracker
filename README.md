# big_sky_match_tracker
# Big Sky Women's Soccer Match Tracker

## Overview
This project helps automate match data entry, statistical tracking, and summary generation for women's soccer matches in the Big Sky Conference.

## Features
- Quick match data entry (teams, players, goals, assists, shots, passes)
- Automatic match summary generation
- Season-long player performance tracking
- Export data to Excel for easy reporting

## Setup
1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python main.py
    ```
4. Enter match data and check `data/` folder for saved files.

## Folder Structure
big_sky_match_tracker/
├── data/                        # All match & season data saved here
├── main.py                       # Main script
├── data_entry.py                 # Data collection
├── match_summary.py              # Match summary
├── stats_tracker.py              # Season stats
├── requirements.txt              # Dependencies
└── README.md                     # Documentation

## Author
Rohith Yadlapalli


