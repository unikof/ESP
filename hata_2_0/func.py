import network
import os
import time

hyphens = "=" * 40 + ">>>"

def connect_wifi():
    
    ssid = "HP2_4"
    password = "harrypotter"
    wlan = network.WLAN(network.STA_IF)
    
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    
    print(hyphens)
    print(f"Scanning networks...")
    networks = wlan.scan()
    found = False
    for net in networks:
        net_ssid = net[0].decode('utf-8')
        print(f"Found: {net_ssid}")
        if net_ssid == ssid:
            found = True
    
    if not found:
        print(f"{ssid} not found!")
        return False
    
    print(f"Connecting to {ssid}...")
    wlan.connect(ssid, password)
    
    print(hyphens)
    
    retries = 0
    while retries < 10:
        status = wlan.status()
        if status == network.STAT_GOT_IP:
            print("CONNECTED !!!")
            print(f"IP: {wlan.ifconfig()}")
            return True
        elif status == network.STAT_CONNECTING:
            print("connecting...")
        elif status == network.STAT_WRONG_PASSWORD:
            print("Incorrect password!")
            return False
        elif status == network.STAT_NO_AP_FOUND:
            print("Access point not found!")
            return False
       
        time.sleep(1)
        retries += 1
    
    print("Timeout (((.....")
    return False
