import time

hyphens = "=" * 30 + ">>>"

print(hyphens)
print("...BOOT STARTED...")

do_update = False

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

    time.sleep(1)

    GD_URL = "https://raw.githubusercontent.com/unikof/ESP/refs/heads/main/Hata/detsk/remote_door/main.py"

    try:
        print("downloading new_main.py...")
        response = urequests.get(GD_URL)
        if response.status_code == 200:
            with open("main.py", "w") as f:
                f.write(response.text)
            print("UPDATE SUCCESS.....")
            print(hyphens)
        else:
            print("downloading failed, status:", response.status_code)
        response.close()
    except Exception as e:
        print("Error:", e)
        print(hyphens)
    finally:
        gc.collect()
        print(hyphens)
        print("5 seconds pause...")
        time.sleep(5)
        print(hyphens)
        print("starting main NOW...")
        print(hyphens)
        import main
else:
    gc.collect()
    print(hyphens)
    print("update SKIPPED, 5 seconds pause...")
    time.sleep(5)
    print(hyphens)
    print("starting main NOW...")
    print(hyphens)
    
    import main
