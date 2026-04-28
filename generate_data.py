import pandas as pd
import random
from datetime import datetime, timedelta

teams = [
    "Arsenal", "Chelsea", "Liverpool", "Man City",
    "Man United", "Tottenham", "Newcastle", "Everton",
    "West Ham", "Leicester", "Brighton", "Villa"
]

data = []

start_date = datetime(2018, 1, 1)

NUM_ROWS = 5000  

for i in range(NUM_ROWS):

    home = random.choice(teams)
    away = random.choice(teams)

    while away == home:
        away = random.choice(teams)

    home_goals = random.randint(0, 5)
    away_goals = random.randint(0, 5)

    date = start_date + timedelta(days=i % 365)

    season = 2018 + (i // 1000)

    data.append([
        home,
        away,
        home_goals,
        away_goals,
        date.strftime("%Y-%m-%d"),
        season
    ])

df = pd.DataFrame(data, columns=[
    "home_team", "away_team",
    "home_goals", "away_goals",
    "date", "season"
])

df.to_csv("data/matches.csv", index=False)

print(f"✅ Dataset created with {len(df)} records")