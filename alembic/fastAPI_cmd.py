# start app
# uvicorn app.main:app

# activate venv
# source path/venv/bin/activate

# upgrade alembic 
# alembic upgrade head
# autogenerate from models
# alembic revision --autogenerate -m "update"
# create revision
# alembic revision -m "message"

# to start heroku app
# heroku ps:restart
# heroku run "alembic upgrade head"-> push changes to postgres instance

# set all env vars in file
# set -o allexport; source /home/lpong/.env; set +o allexport