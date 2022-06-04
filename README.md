# website-parse-to-telegram
parse content from a website and send it as a message via telegram to a channel/group periodically

it works against the cloudflare protection

quick guide for setting up a telegram bot:
https://medium.com/codex/telegram-http-api-with-python-sending-messages-programatically-28be2e04bbcd

made for python3

## Installation

Just clone the script onto your machine

## Usage

edit `scheduletime` to change the period between the execution

`url` : website url

`parse.find_all()` to choose which element to parse

`bot_token` `bot_chatID`: setup the telegram bot
