from slackbot.bot import respond_to
from slackbot.bot import listen_to
import subprocess
import re 

from imgurpython import ImgurClient
import os
import ConfigParser

snakebot_config = None

def upload_to_imgur():
	global snakebot_config

	def perform_actual_upload():
		# If you already have an access/refresh pair in hand
		client_id = snakebot_config.get("imgur", "client_id")
		client_secret = snakebot_config.get("imgur", "client_secret")
		access_token = snakebot_config.get("imgur", "access_token")
		refresh_token = snakebot_config.get("imgur", "refresh_token")

		# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
		client = ImgurClient(client_id, client_secret, access_token, refresh_token)

		path = os.path.join(os.path.expanduser("~"), "Pictures/3dprinter", "photo.jpg")
		print "Uploading from ", path
		result = client.upload_from_path(path, anon=False)
		print result['link']

		return result['link']

	if snakebot_config is not None:
		return perform_actual_upload()
	else:
		curr_dir = os.path.dirname(os.path.realpath(__file__))
		snakebot_config = ConfigParser.ConfigParser()
		snakebot_config.read( os.path.join(curr_dir, "..","config.ini") )
		print snakebot_config.sections()
		return perform_actual_upload()



@respond_to('pic', re.IGNORECASE)
def post_pic(message):
		print "Taking pic..."
		subprocess.call(["take_photo.sh"], shell=True)
		message.reply('Taking pic, please wait...')
		link = upload_to_imgur()
		message.reply("Link %s" % (link))
