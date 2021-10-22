#!/usr/bin/env python3

from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep
from datetime import datetime
import sys
import argparse

# FUNCTION TO DEAL WITH NEGATIVE MILLISECONDS INPUT
def check_positive(value):
    ivalue = float(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s : milliseconds cannot be negative !" % value)
    return ivalue

def send_message(args):
	connection = HTTPSConnection("discordapp.com", 443)
	header_data = { 
		"content-type": "application/json", 
		"user-agent": args.user_agent, 
		"authorization": args.token, 
		"host": "discordapp.com"
	}
	message_data = { 
		"content": args.message, 
		"tts": "false",
	}
	try: 
		connection.request("POST", f"/api/v8/channels/{args.channel}/messages", dumps(message_data), header_data) 
		resp = connection.getresponse() 
		if 199 < resp.status < 300: 
			print(f"Message '{args.message} sent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") 
			pass 
		else: 
			stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n") 
			pass
	except: 
		stderr.write("Failed to send_message\n") 	
 
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-ua", "--user-agent", type=str, default="Mozilla/5.0", help="User agent used by the program, default value : Mozilla/5.0")
	parser.add_argument("-t", "--token", type=str, help="Your discord user token, it's up to you to find it !", required=True)
	parser.add_argument("-m", "--message", type=str, help="The message you want to post on the channel", required=True)
	parser.add_argument("-ms", "--milliseconds", type=check_positive, help="Time in milliseconds between each message (a good valud is 1000 for 1 second)", required=True)
	parser.add_argument("-c", "--channel", type=str, help="Id of the discord channel, again, it's up to you to find it (google is your friend) !", required=True)
	try:
		args = parser.parse_args()
	except:
		sys.exit(1)
	while True:     			# Infinite loop 
		send_message(args)      # Send the message 
		sleep(args.milliseconds) 	# Wait X milliseconds to repeat