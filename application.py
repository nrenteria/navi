from flask import Flask, render_template, url_for, flash, request, redirect
from flask_sqlalchemy import SQLAlchemy
from tasks import send_message, parse_datetime
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def schedule_message(phoneNumber, message):
    send_message(phoneNumber, message)
    return

@app.route('/', methods=['GET'])
def index():
    return render_template('sms2.html')

@app.route("/done", methods=['POST'])
def done():
    phoneNumber = request.form['phone']
    reminderTimeInput = request.form['remindertime']
    message = request.form['message']

    if len(phoneNumber) == 10 and int(phoneNumber):
        reminderTime = parse_datetime(reminderTimeInput)
        schedule_message.apply_async(args=[phoneNumber, message], eta = reminderTime)
        flash("Reminder is scheduled!")
        return redirect(url_for('index'))
    else:
        flash("Unable to schedule reminder. Please try again.")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key='+\x0e\xeb\xc57>\xb9\x0b\xaf\xb8}U\xbc6t\xaf(T\xbe\x12\xbaT\x80>'
    app.run(debug=True)
