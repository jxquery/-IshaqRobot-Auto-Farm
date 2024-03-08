from telethon.sync import TelegramClient, events

import os

import random

import time



print('                           AF STARTED | MADED BY @JAXQUERY     ')

group = 'IshaqRobot'

api_id = 24505591

api_hash = 'feb2fb30318cc9e7595390fb625e3285'

while True:
	 with TelegramClient('IshaqRobot', api_id, api_hash) as client:
	 	client.send_message(group, 'кф снять')
	 	time.sleep(180)
	 	
	 	client.run_until_disconnected()
