# Iketel_back

Backend part of Iketel platform for storymaking with AI.

For Windows:

Download the repository

`git clone https://github.com/KD-TrendOn/Iketel_back`

Put your .env file into repo

Required fields:

SECRET_KEY = (execute openssl rand -hex 32)

ALGORITHM = HS256

ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/iketel_db

`cd Iketel_back`

`python -m venv env`

`env\Scripts\Activate.ps1`

`pip install -r requirements.txt`

`uvicorn main::app --reload`

Now your API is running!

For devs:

after shutdowning the server(don't forget to check if you inside virtual environment)

`pre-commit install`

`pre-commit`

