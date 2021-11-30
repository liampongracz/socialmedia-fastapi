# start app
# uvicorn app.main:app

# activate venv
# source path/venv/bin/activate

# upgrade alembic 
# alembic upgrade head
# autogenerate from models
# alembic revision --autogenerate -m "update"

# to start heroku app
# heroku ps:restart
# heroku run "alembic upgrade head"