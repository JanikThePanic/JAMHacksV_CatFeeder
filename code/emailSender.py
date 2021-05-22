import smtplib, os
from dotenv import load_dotenv

load_dotenv()

def sendEmail():
	sender = os.getenv('EMAILSENDER')
	password = os.getenv('PASSWORD')
	message = "Subject: Masha's Food \nMy dearest Janik. \n\nI am out of thy food, and am requesting to the highest honor to be fed. \n\nMuch appreciated, \nMasha."
	email = 'jk4abdl@gmail.com'

	s = smtplib.SMTP_SSL('smtp.gmail.com')
	s.login(sender, password)
	s.sendmail(sender, email, message)
	s.quit()

if __name__ == "__main__":
	sendEmail()