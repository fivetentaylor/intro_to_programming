# Let's play with the Coinbase API

Get a list of their products using the RESTful api

```
python get_products.py
```

Get some real time data using their websocket api. Going to just grab a cli tool written in node to stream json over a pipe

Install the tool with

```
brew install node
npm install --global coinbase-pro-feed
```

The run our script like so

```
coinbase-pro-feed BTC-USD | python coinbase/format_wss_feed.py
```
