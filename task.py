from twilio.rest import Client

account_sid = 'TWILIO ACCOUNT SID'
auth_token = "TWILIO AUTH TOKEN"
client = Client(account_sid, auth_token)

def send_message(phoneNumber, url):
	try:
		message = client.messages.create(
			body = url,
			from_ ="+12563776973",
			to = "+1" + phoneNumber
			)
		return True
	except:
		return False