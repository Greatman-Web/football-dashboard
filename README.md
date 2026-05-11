#Football Analytics Dashboard

A Flask-based web application that loads and analyses football match
data from open datasets.Users can search teams, view match results, and analyse performance
statistics.

##Live Demo
https://football-dashboard-7ed0.onrender.com
Note that when you click on this website, it does not just appear immediately, it shows you a render page showing you that your application is loading, after that the web pages display and the application is functional. This is because i am using the free render web service.

##Features

-Team search with autocomplete suggestions
-Match results display (home vs away)
-Win / Loss / Draw statistics
-Goals scored and conceded tracking
-Match history from open dataset
-Modern dark-themed UI dashboard
-Fully deployed on Render


##Tech Stack

-Python (Flask)
-SQLAlchemy (ORM)
-SQLite Database
-HTML, CSS, JavaScript
-Pandas (data loading)
-Render (deployment)
-Git (version control)

##Project Structure

Football_dashboard/
│
├── app.py
├── models.py
├── load_data.py
├── generate_data.py
├── reset_db.py
├── test_app.py
├── football.db
│
├── templates/
│   ├── index.html
│   ├── results.html
│   ├── 404.html
│   └── 500.html
│
├── static/
│   └── style.css
│
├── data/
│   ├── epl_2018.csv
│   ├── epl_2019.csv
│   ├── epl_2020.csv
│   ├── epl_2021.csv
│   ├── epl_2022.csv
│   ├── epl_2023.csv
│   └── epl_2024.csv
│
└── README.md



##Data Source

This project uses open English Premier League datasets from multiple seasons:

-2018–2025 seasons
-Over 2500+ match records

Each dataset includes:
-Home team
-Away team
-Goals scored
-Match date
-Season information

##Installation & Setup

``` bash
git clone https://github.com/Greatman-Web/football-dashboard
cd football-dashboard
pip install -r requirements.txt
python load_data.py
python app.py
```

##Testing
Basic route testing included and implementing pytest in order to test consistently.

##Error Handling
-Custom 404 page
-Custom 500 handler
-Input validation

##Deployment (Render)

-Connect GitHub repo
-Build: pip install -r requirements.txt
-Start: python app.py

##Author
Greatman Amadimati
2026
