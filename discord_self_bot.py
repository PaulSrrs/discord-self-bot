#!/usr/bin/env python3

from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
from datetime import datetime
import sys
import argparse

# FUNCTION TO DEAL WITH NEGATIVE SECONDS INPUT
def check_positive(value):
    ivalue = float(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s : seconds cannot be negative or equal to 0 !" % value)
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
	parser.add_argument("-w", "--wait", type=check_positive, help="Time in seconds between each message. Only one message will be send if not submitted.")
	parser.add_argument("-t", "--token", type=str, help="[required] Your discord user token, it's up to you to find it !", required=True)
	parser.add_argument("-m", "--message", type=str, help="[required] The message you want to post on the channel", required=True)
	parser.add_argument("-c", "--channel", type=str, help="[required] Id of the discord channel, again, it's up to you to find it (google is your friend) !", required=True)
	try:
		args = parser.parse_args()
	except:
		sys.exit(1)
	if (args.wait is not None):
	    while True or args.wait:     			# Infinite loop
		    send_message(args)      			# Send the message
		    sleep(args.wait)                    # Wait X seconds
	else:
	    send_message(args)
