import os
from dotenv import load_dotenv

APP_STATE = os.environ.get('APP_STATE')

#This variable should be set when running in standalone without docker
if APP_STATE == "standalone":
    print("APP STATE: Standalone")
    load_dotenv(".env-standalone")

#This variable should be set when in development mode with docker
if APP_STATE == "development":
    print("APP STATE: Development")
    load_dotenv(".env-dev")

if APP_STATE == "production":
    #Use .env-dev or .env-standalone as example
    #suggestion is to include this on server and not in git repo
    print("APP STATE: Production")
    load_dotenv(".env-prod")

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('MY_SECRET_KEY') or 'mytopsecretkey'
    EVENT_APP_SERVER = os.environ.get('EVENT_APP_SERVER')
    TODO_APP_SERVER = os.environ.get('TODO_APP_SERVER')
    BLOG_APP_SERVER = os.environ.get('BLOG_APP_SERVER')
    
