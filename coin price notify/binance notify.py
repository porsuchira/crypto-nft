import requests

def get_price():
  url = 'https://api3.binance.com/api/v3/ticker/price?symbol='
  coin = {'BTC' : 'BTCUSDT','ETH' : 'ETHUSDT'}
  msg = ''

  try:
    for i in coin:
      headers = {
          'Content-Type': 'application/json'
      }
      response = requests.get(url+coin[i], headers=headers)
      price = response.json()
      price = round(float(price["price"]),3)
      #print(f'{price}')
      msg += '\n {} = ${}'.format(i,price)
    send_notify(msg)
      
  except Exception as e:
    print(e)

def send_notify(msg):
  sticker = '&stickerPackageId=8522&stickerId=16581281'
  url = 'https://notify-api.line.me/api/notify?message={}{}'.format(msg, sticker)
  token  = 'token'
  headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Bearer {}'.format(token)
  }
  response = requests.post(url, headers = headers, data = msg)
  print(response.text)

get_price()
