# HOCKEY STATS API

This project is meant to act as a hockey stat api that highlights the full understanding and use of CRUD. This project contains contains a rest api designed to log hockey stats with the option to CREATE, READ, UPDATE, and DELETE.

## Features
- Contains json on a webpage (LocalHost:5000)
- Ability to add, update, delete players

## Project Structure
```
hockey-stats-api/
├── app.py
├── requirements.txt
├── database.py
├── README.md
├── .gitignore
├── data/
│   └── practice.db
└── sample_data/
    ├── games.csv
    ├── players.csv
    └── player_stats.csv
```
## How To Install And Run
- Clone the repo from GitHub
    git clone <repository-url>
- Navigate to hockey-stats-api
- Install dependencies
    pip install -r requirements.txt
- Set up the database
    python database.py
- Seed the database
    python seed.py
- Run the app
    python app.py

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | /api/players | Returns all players |
| GET | /api/player/<id> | Returns single player |
| GET | /api/games | Returns all games |
| GET | /api/player_stats | Returns all player stats |
| POST | /api/players | Adds a new player |
| PUT | /api/players/<id> | Updates a player |
| DELETE | /api/players/<id> | Deletes a player |

## Technologies Used
- Python 3
- Flask - web framework
- SQLite - database storage
- JSON - data format for API responses
- Postman - Rest API app

## What I Learned
I learned how to build a Rest API. I'm also learning and understanding CRUD and how to incorporate it within projects. Throughout this project, I also learned how to better set up a repo structure to help myself remain organized. When creating the Rest API, I learned how to use Flask along with a request/response cycle as well as GET, POST, PUT and DELETE. I learned what makes a REST API different than just returning HTML which is returning JSON so it can be used across all apps. Also how to utilize CRUD for updating, adding, deleting data from the table found on the endpoints. If I continued on with this, I would like to add endpoints for games and player stats using CRUD and add authentication so only authorized users can POST/PUT/DELETE.