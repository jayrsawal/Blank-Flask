# -*- coding: utf-8 -*-
import sys
sys.path.append("./static/py")
import os
import db
import codecs
import simplejson as json
import cPickle as pickle
import numpy as np
import common as cm
import constants as CONST
import re
import nltk
import time
from pathlib2 import Path
from sklearn.feature_extraction.text import CountVectorizer
from lz4.frame import compress, decompress
from flask import *
from lxml import etree


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = CONST.UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# Common variables
db = db.Database()

@app.route("/")
def index():    
    return render_template("index.html")

if __name__ == "__main__":
    sess.init_app(app)
    app.run(debug=True)
