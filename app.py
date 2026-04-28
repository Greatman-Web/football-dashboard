from flask import Flask, render_template, request, jsonify
from models import db, Team, Match

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///football.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/search')
def search():

    team_name = request.args.get('team')

    # ❌ Empty input → 404
    if not team_name:
        return render_template("404.html"), 404

    # 🔍 STRICT SEARCH (important for tests)
    team = Team.query.filter(Team.name.ilike(team_name)).first()

    # ❌ Team not found → 404
    if team is None:
        return render_template("404.html"), 404

    matches = Match.query.filter(
        (Match.home_team_id == team.id) |
        (Match.away_team_id == team.id)
    ).all()

    # 🔥 STATS INIT
    wins = 0
    losses = 0
    draws = 0
    goals_scored = 0
    goals_conceded = 0

    for m in matches:

        # HOME TEAM CASE
        if m.home_team_id == team.id:

            goals_scored += m.home_goals
            goals_conceded += m.away_goals

            if m.home_goals > m.away_goals:
                wins += 1
            elif m.home_goals < m.away_goals:
                losses += 1
            else:
                draws += 1

        # AWAY TEAM CASE
        else:

            goals_scored += m.away_goals
            goals_conceded += m.home_goals

            if m.away_goals > m.home_goals:
                wins += 1
            elif m.away_goals < m.home_goals:
                losses += 1
            else:
                draws += 1

    return render_template(
        "results.html",
        team=team,
        matches=matches,
        wins=wins,
        losses=losses,
        draws=draws,
        goals_scored=goals_scored,
        goals_conceded=goals_conceded
    )


@app.route('/teams')
def get_teams():
    teams = Team.query.all()
    return jsonify([t.name for t in teams])


# ✅ ERROR HANDLERS
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)