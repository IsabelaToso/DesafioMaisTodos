from app import app
from flaskext.mysql import MySQL

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'isa24337289'
app.config['MYSQL_DATABASE_DB'] = 'desafiomaistodos'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)
