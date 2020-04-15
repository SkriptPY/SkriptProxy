# Proxy On
import os

proxy = "proxy.example.com"
port = 8080

def Proxy_on():
    os.system('networksetup -setwebproxy Ethernet '+proxy+' '+port)

Proxy_on()

# Thanks to Mahmoud Al-Nafei on Stackoverflow
# If the network service isn't named just "Ethernet", you may need to parse networksetup -listallnetworkservices or -listnetworkserviceorder to get the correct name.
