import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

APP_STATE = os.environ.get('APP_STATE')

if APP_STATE == "standalone":
    print("APP STATE: Standalone")
    load_dotenv(".env-standalone")

if APP_STATE == "development":
    print("APP STATE: Development")
    load_dotenv(".env-dev")

# not included and should be placed on server and not in git repo
if APP_STATE == "production":
    print("APP STATE: Production")
    load_dotenv(".env-prod")

class Config:
    SECRET_KEY = os.environ.get('MY_SECRET_KEY') or 'mytopsecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

