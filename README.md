# Navi - SMS Reminders using Flask, Celery, and Twilio
This repository contains the example code for the Navi web app

![Web App](https://github.com/nrenteria/navi/blob/master/image.JPG)

# Quick Setup
1. Clone this repository.
2. Create a virtualenv: virtualenv venv
3. Enter into the virtual environment: source venv/bin/activate
4. Install the requirements: pip install -r requirements.txt
3. Open a second terminal window and start a local Redis server within virtual environment (for ubuntu: $redis-server)
4. Insert personal Twilio info into tasks.py (must put in info before starting celery job queue)
5. Open a third terminal window and start a Celery worker within virtual environment: celery -A application.celery worker --loglevel=info
6. Start the Flask application on your original terminal window: python3 application.py
7. Go to http://localhost:5000/ to start this application!
