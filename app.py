from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Stops

@app.route('/')
def hello():
	# workPlease = stops.query.all()
	# print(workPlease)
	return "Hello World!"

if __name__ == '__main__':
	app.run()
