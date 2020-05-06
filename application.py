from flask import Flask, render_template, url_for, flash, request, redirect
from flask_sqlalchemy import SQLAlchemy
from task import send_message

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('sms2.html')

@app.route("/done", methods=['POST'])
def done():
    phoneNumber = request.form['phone']
    reminderTime = request.form['remindertime']
    zoomLink = request.form['url']

    if send_message(phoneNumber, zoomLink):
        flash("Text has been sent!")
        return redirect(url_for('index'))
    else:
        flash("Text message was unable to send. Try again.")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key='+\x0e\xeb\xc57>\xb9\x0b\xaf\xb8}U\xbc6t\xaf(T\xbe\x12\xbaT\x80>'
    app.run(debug=True)