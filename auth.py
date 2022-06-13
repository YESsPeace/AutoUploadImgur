import webbrowser

import pyimgur

CLIENT_ID = "7d220f48ce3309b"
CLIENT_SECRET = "84f69bb1dd11888555837fefbe816a13d3e28625"   # Needed for step 2 and 3

im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
auth_url = im.authorization_url('pin')
webbrowser.open(auth_url)
pin = input("What is the pin? ") # Python 3x
#pin = raw_input("What is the pin? ") # Python 2x

access_token, refresh_token = im.exchange_pin(pin)

token_file = open('tokens.txt', 'w')
token_file.write(str(access_token) + '\n' + str(refresh_token))