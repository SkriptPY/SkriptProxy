# Proxy On
import os

proxy = "proxy.example.com"
port = 8080

def Proxy_on():
    os.system('networksetup -setwebproxy Ethernet '+proxy+' '+port)

Proxy_on()

# Thanks to Mahmoud Al-Nafei on Stackoverflow
