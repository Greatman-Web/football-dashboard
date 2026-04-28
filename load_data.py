import pandas as pd
from app import app
from models import db, Team, Match

import pandas as pd
from app import app
from models import db, Team, Match

with app.app_context():
    db.drop_all()
    db.create_all()

print("🔥 Loading multiple seasons...")

files = [
    "data/epl_2018.csv",
    "data/epl_2019.csv",
    "data/epl_2020.csv",
    "data/epl_2021.csv",
    "data/epl_2022.csv",
    "data/epl_2023.csv",
    "data/epl_2024.csv"
]

df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

print(f"📊 Total rows loaded from CSV: {len(df)}")

with app.app_context():

    team_cache = {}

    # 🟢 CREATE TEAMS FIRST
    for team_name in pd.concat([df["HomeTeam"], df["AwayTeam"]]).unique():

        team = Team.query.filter_by(name=team_name).first()

        if not team:
            team = Team(name=team_name)
            db.session.add(team)
            db.session.flush()

        team_cache[team_name] = team.id

    print("✅ Teams inserted")

    # 🟢 CREATE MATCHES
    for _, row in df.iterrows():

        match = Match(
            home_team_id=team_cache[row["HomeTeam"]],
            away_team_id=team_cache[row["AwayTeam"]],
            home_goals=row["FTHG"],
            away_goals=row["FTAG"],
            date=row["Date"]
        )

        db.session.add(match)

    db.session.commit()

    db.session.commit()

print("🎯 Matches inserted successfully!")

with app.app_context():
    print(f"✅ Final match count: {Match.query.count()}")