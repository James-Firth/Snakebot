# Snakebot

A Slack bot that uploads webcam photos to imgur

## Requirements

#### Program/Libraries
* [imgurpython](https://github.com/Imgur/imgurpython) - official imgur library
* [slackbot](https://github.com/lins05/slackbot) - community slackbot library
* [fswebcam](http://manpages.ubuntu.com/manpages/wily/man1/fswebcam.1.html) - A small and simple webcam for *nix. Used in the `take_photo` script

#### API Keys

* Slack Bot API Token
* [Imgur API Keys](https://api.imgur.com/)
  * Register your application [here](https://api.imgur.com/oauth2/addclient) (when logged in).
  * I used "OAuth 2 authorization without a callback URL"
  * Now that you ahvea client ID and Client secret you will need to modify this url:
    https://api.imgur.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&response_type=token&state=woo_bot_works
  * Replace `YOUR_CLIENT_ID` with your new Client ID
  * Visit the new link
  * Copy the URL after the redirect
    It should look something like `https://imgur.com/?state=woo_bot_works#access_token=XXX&expires_in=2419200&token_type=bearer&refresh_token=YYY&account_username=JamesFirth&account_id=0000`
  * Use the `access_token` and `refresh_token` in the config.ini file.
  