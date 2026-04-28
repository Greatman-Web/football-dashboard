from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# =========================
# TABLE 1: TEAMS
# =========================
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # relationships
    home_matches = db.relationship(
        'Match',
        foreign_keys='Match.home_team_id',
        backref='home_team_ref',
        lazy=True
    )

    away_matches = db.relationship(
        'Match',
        foreign_keys='Match.away_team_id',
        backref='away_team_ref',
        lazy=True
    )


# =========================
# TABLE 2: MATCHES
# =========================
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    home_goals = db.Column(db.Integer)
    away_goals = db.Column(db.Integer)
    date = db.Column(db.String(50))