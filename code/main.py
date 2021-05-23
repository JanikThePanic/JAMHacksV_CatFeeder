from emailSender import *
from catDetection.v2.videoCatDetection import *
from datetime import datetime, timedelta
import serial
import time

def checkFeedingChange(feedingTime, state):
	# if what we entered the loop in is different what we are in right now
	# means there was a change
	if feedingTime != state:
		feedingTime = state
		# CODE TO SEND TOGGLE SIGNAL
		arduino.write(str("t").encode())
		print('t')

def main(timeOverride = False):
	# make serial connection
	global arduino
	arduino = serial.Serial('COM4', 9600)
	arduino.reset_input_buffer()
	data = arduino.readline().decode("utf-8")

	# it takes like 2 seconds for the arduino to start once connected to
	time.sleep(2.5)

	# main script that is always running
	# first, check the time. if it is feeding time then check if the cat exists. if true give food
	# after giving food check the level of the food. if low send janik an email

	feedTimes = [7, 13, 19]
	if timeOverride:
		feedTimes = range(24)

	# if we start the program in feeding time, it needs to reflect that
	# so when we toggle, we start with the correct state
	feedingTime = (bool)(datetime.now().hour in feedTimes)
	if feedingTime:
		arduino.write(str("t").encode())
		print('t')

	
	fedThisSession = False
	while True:
		# read serial from arduino
		oldData = data
		data = arduino.readline().decode("utf-8")
		data = data[0]
		# just print everything for troubleshooting
		print(data)

		# if f is in the datastream then it needs to be filled
		if (data == 'f' and oldData != 'f'):
			sendEmail()

		if (datetime.now().hour in feedTimes) and (not fedThisSession):
			# check if we JUST entered feeding time
			# give true as we are in feeding time
			checkFeedingChange(feedingTime, True)

			# this will start video feed, and run in a while loop until masha is found
			catFound = checkForCat()

			if catFound:
				fedThisSession = True

				# JANIK FEED YOUR CAT HERE
				arduino.write(str("p").encode())
				print('p')

		elif not (datetime.now().hour in feedTimes):
			# check if we just left feeding time
			# gives false as we are out of feeding time
			checkFeedingChange(feedingTime, False)
			# resets fed
			fedThisSession = False


if __name__ == '__main__':
	main()