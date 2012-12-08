from flask import Flask,render_template,request,redirect,url_for,abort,session,jsonify
from flask_config import flask_secret_key
import requests
import json

app = Flask(__name__,static_path='/static/')
#never enable this when externally visible
#app.config['DEBUG']=True
app.config['SECRET_KEY']=flask_secret_key

@app.route('/')
def data_input():
    app.logger.error(request.query_string)
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run()
