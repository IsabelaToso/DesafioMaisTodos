from flask import Flask
from flask_cors import CORS, cross_origin

#codificando instancia do Flask
app = Flask(__name__)
CORS(app)
