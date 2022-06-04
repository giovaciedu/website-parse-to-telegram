#libraries
import requests
import httpx
import schedule
import time
from lxml import html
from bs4 import BeautifulSoup

scheduletime = 180 # execute the function every "scheduletime"

def report_url():
    # Put your URL here
    url = ''
    # Fetching the html
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'
    headers = {"user-agent": user_agent}
    req = httpx.get(url, headers=headers)
    print(req)
    parse = BeautifulSoup(req.text, 'html.parser')    # Parsing the html
    # Provide html elements' attributes to extract the data
    textpar = parse.find_all('h6')  # h6 as example
    strtext = str(textpar)
    #strtextu = strtextu.replace("<h6>","")   <- clean text
    #strtextu = strtextu.replace("</h6>","")
    # Send a message via a telegram bot
    bot_token =  '<token>'  # YOUR_BOT_TOKEN
    bot_chatID = '<chat_id>'  # TELEGRAM_USER_CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + strtext
    response = requests.get(send_text)
    return response.json()
    
report_url()    
schedule.every(scheduletime).seconds.do(report_url)
while True:
    schedule.run_pending()
    time.sleep(1)
    