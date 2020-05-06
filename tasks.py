from twilio.rest import Client
import datetime as dt
from dateutil import tz
import re

account_sid = 'TWILIO ACCOUNT SID'
auth_token = "TWILIO AUTH TOKEN"
client = Client(account_sid, auth_token)

def send_message(phoneNumber, message):
	message = client.messages.create(
		body = message,
		from_ ="TWILLIO NUMBER",
		to = "+1" + phoneNumber
		)
	
def parse_datetime(datetime):
	tZone = tz.gettz()
	values = re.split("-|T|:", datetime)
	year = int(values[0])
	month = int(values[1])
	day = int(values[2])
	hour1 = int(values[3])
	minute1 = int(values[4])
	reminderTime = dt.datetime(year, month, day, hour = hour1, minute = minute1, tzinfo = tZone)
	return reminderTime
