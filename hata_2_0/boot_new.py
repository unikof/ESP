import time
import ntptime
import machine

hyphens = "=" * 40 + ">>>"

print(hyphens)
print("...BOOT STARTED...")

do_update = True

print(hyphens)
print("5 seconds pause for cancelling...")
time.sleep(5)
print(hyphens)

if(do_update):
    print("update activated...")
    
    import network
    import urequests
    import os
    import gc
    import time
    import socket

    SSID = "HP2_4"
    PASSWORD = "harrypotter"

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    while not wifi.isconnected():
        time.sleep(1)

    print("WiFi OK, network config:", wifi.ifconfig())
    print(hyphens)

    time.sleep(3)

    try:
        print("downloading new_main.py...")
        response = urequests.get("http://raw.githubusercontent.com/unikof/ESP/main/hata_2_0/zal/wall/main.py")
        if response.status_code == 200:
            print("response_status: 200")
            with open("main.py", "w") as f:
                f.write(response.text)
            print("UPDATE MAIN SUCCESS.....")
            print(hyphens)
        else:
            print("downloading failed, status:", response.status_code)
        response.close()
    except Exception as e:
        print("Error:", e)
        print(hyphens)
        
    try:
        print("downloading new_addr.py...")
        response = urequests.get("http://raw.githubusercontent.com/unikof/ESP/main/hata_2_0/addr.py")
        if response.status_code == 200:
            print("response_status: 200")
            with open("main.py", "w") as f:
                f.write(response.text)
            print("UPDATE ADDR SUCCESS.....")
            print(hyphens)
        else:
            print("downloading failed, status:", response.status_code)
        response.close()
    except Exception as e:
        print("Error:", e)
        print(hyphens)
        
    try:        
        ntptime.host = "pool.ntp.org"
        ntptime.settime()
        print("NTP time sync OK")
    except Exception as e:
        print("Error:", e)
        print(hyphens)
        
    finally:
        gc.collect()
        print("starting main NOW..........")
        import main
else:
    gc.collect()
    print(hyphens)
    print("update SKIPPED...")
    print(hyphens)
    print("starting main NOW..........")
    
    import main


