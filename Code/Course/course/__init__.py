from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message, Attachment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sandescolab@gmail.com'
app.config['MAIL_PASSWORD'] = '9656257368Ss!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_ASCII_ATTACHMENTS'] = True
mail = Mail(app)
db = SQLAlchemy(app)


from course import routes