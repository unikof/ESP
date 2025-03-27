print("Boot started...")

import network
import urequests
import os
import gc
import time

SSID = "HP2_4"
PASSWORD = "harrypotter"

import network
import urequests
import os
import gc
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    time.sleep(1)

print("Wi-Fi connected...")

GD_URL = "https://raw.githubusercontent.com/unikof/ESP/refs/heads/main/Hata/detsk/remote_door/main.py"

try:
    print("Downloading new_main.py...")
    response = urequests.get(GD_URL)
    if response.status_code == 200:
        with open("new_main.py", "w") as f:
            f.write(response.text)
        print("Update success....")
    else:
        print("Failed, status:", response.status_code)
    response.close()
except Exception as e:
    print("Error:", e)

gc.collect()

#import main
