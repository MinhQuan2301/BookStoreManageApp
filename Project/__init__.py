from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
app = Flask(__name__, template_folder='template')
app.secret_key = "1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm,./ASDFGHJKLZMXNCBVQWERTYUIOP"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/dbproject?charset=utf8mb4" % quote("d@Ikaquan2301")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app=app)
