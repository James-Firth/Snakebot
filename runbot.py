#!/usr/bin/python
from slackbot.bot import Bot
import slackbot.settings as settings
import logging
import sys
import os

#for config loading
import ConfigParser

def main():
	global snakebot_config
	logging.basicConfig()
	curr_dir = os.path.dirname(os.path.realpath(__file__))
	sys.path.append(curr_dir)

	snakebot_config = ConfigParser.ConfigParser()
	snakebot_config.read("config.ini")

	settings.API_TOKEN = snakebot_config.get("slack", "API_TOKEN")

	settings.PLUGINS = ["snakebot"] #Overwrites other plugins. Don't need upload for instance.
	bot = Bot()
	print "[[ Snakebot online ]]"
	bot.run()

def setup_config():
	sconfig = ConfigParser.ConfigParser()
	print "Performing first time setup..."
	API_TOKEN = raw_input("Please enter your slack API_TOKEN:")

	client_id = raw_input("Please enter your imgur client_id:")
	client_secret = raw_input("Please enter your imgur client_secret:")
	access_token = raw_input("Please enter your imgur access_token:")
	refresh_token = raw_input("Please enter your imgur refresh_token:")

	sconfig.add_section("slack")
	sconfig.set("slack", "API_TOKEN", API_TOKEN)

	sconfig.add_section("imgur")
	sconfig.set("imgur", "client_id", client_id)
	sconfig.set("imgur", "client_secret", client_secret)
	sconfig.set("imgur", "access_token", access_token)
	sconfig.set("imgur", "refresh_token", refresh_token)

	with open("config.ini", "w") as f:
		sconfig.write(f)


	return

if __name__ == "__main__":
	if os.path.isfile("config.ini"):
		print "Running bot..."
		main()
	else:
		setup_config()
		print "Setup complete, running bot..."
		main()
