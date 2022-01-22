<h1 align="center">OpenStream</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/24627876/150639537-d971ba09-3ae0-40bf-9416-ac568f3c2b8d.png" />
  <br>
  <i>A data analyzer for Opensea.io website using mitmproxy and pandas <br> to analyze performing collection and share data with users through telegram channels</i>
  <br>
</p>

<p align="center">
  <a href="https://discord.gg/hBzvYeWn">
    <img src="https://img.shields.io/discord/933752833398956032.svg?logo=discord&logoColor=fff&label=Discord&color=7389d8" alt="Discord conversation" />
  </a>&nbsp;
  <img src="https://img.shields.io/github/pipenv/locked/python-version/anonbeat1/OpenStream?logo=python&logoColor=fff" alt="Python version" />
  &nbsp;
  <a href="https://t.me/privateStreamOpensea">
    <img src="https://img.shields.io/badge/Bot-Opensea__Private__Stream__Trend-blue?logo=telegram&logoColor=fff" alt="Telegram bot" />
    &nbsp;
  </a>
</p>
  
<hr>

## Setting Up a Project (follow each step in sequence!!)

### Prerequisites
- Install [mitmproxy]
- Install [requirements.txt]
  ```
    cd OpenStream
    pip3 install -r requirements.txt
  ```

## Start to track every transaction on 5 minutes

Config local proxy:
  - address: <kbd>localhost</kbd>
  - port: <kbd>8080</kbd>

<br>

Start mitmproxy: 
```
  mitmproxy -s RequestStream.py
```

<br>

Open page on any browser:
- [OpenSea activity] (page activity, filter by chain eth)
<br>

Every 5 minutes, you can find the response in data.txt file (is auto-generated)

## If you want to try it with your own telegram channel

Set into [Opensea_Stream_Analyzer.ipynb] 
  - <kbd>TELEGRAM_TOKEN</kbd>
  - <kbd>CHAT_ID</kbd>

Set into [TwitterCaller.py]
  - <kbd>TWITTER_TOKEN</kbd>

Start:
- [Opensea_Stream_Analyzer.ipynb] (with jupyter-notebook or ide like vs.code)

## Community

Join the conversation and help the community.

- [Discord][discord]

## Buy Me A Coffee

 - ETH: 0xD528F629fc4165458BBba6c7ff889C29a951aebF
 - BTC: 3EkUnn9jpnPLZDMnwgScMtTtvJZXuD4UYw

<a href="https://www.buymeacoffee.com/spilotrica1">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>


[discord]: https://discord.gg/hBzvYeWn
[OpenSea activity]: https://opensea.io/activity?search[chains][0]=ETHEREUM
[mitmproxy]: https://mitmproxy.org/
[requirements.txt]: requirements.txt
[Opensea_Stream_Analyzer.ipynb]: Opensea_Stream_Analyzer.ipynb
[TwitterCaller.py]: TwitterCaller.py
