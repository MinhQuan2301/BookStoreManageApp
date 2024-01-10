from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='template')
# app = Flask(__name__, template_folder='template/layout')
app.secret_key = "1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm,./ASDFGHJKLZMXNCBVQWERTYUIOP"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/dbproject?charset=utf8mb4" % quote("d@Ikaquan2301")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2


db = SQLAlchemy(app=app)


import cloudinary

cloudinary.config(
    cloud_name="dbg9hkyzp",
    api_key="959857527741799",
    api_secret="cCdgrCh8gKFRgvKu3-vBS4-L3Pk"
)