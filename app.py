import os
from flask import Flask, render_template, url_for, flash, request, redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy

from celery import Celery

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('sms2.html')


if __name__ == "__main__":
    app.run(debug=True)
