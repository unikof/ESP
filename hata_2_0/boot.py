import time
import func
import ntptime
import machine
import urequests

hyphens = "=" * 40 + ">>>"

print(hyphens)
print("...BOOT STARTED...")

do_update = True

print(hyphens)
print("5 seconds pause for cancelling...")
time.sleep(5)

if do_update and func.connect_wifi():
    print("update activated...")
  
    try:
        print("downloading new main.py...")
        response = urequests.get("https://raw.githubusercontent.com/unikof/ESP/main/hata_2_0/zal/light/main.py")
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
        print("downloading new addr.py...")
        response = urequests.get("https://raw.githubusercontent.com/unikof/ESP/main/hata_2_0/addr.py")
        if response.status_code == 200:
            print("response_status: 200")
            with open("addr.py", "w") as f:
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
        print("downloading new func.py...")
        response = urequests.get("https://raw.githubusercontent.com/unikof/ESP/main/hata_2_0/func.py")
        if response.status_code == 200:
            print("response_status: 200")
            with open("func.py", "w") as f:
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

    gc.collect()
    print("starting main NOW..........")
    import main
else:
    gc.collect()
    print(hyphens)
    print("update SKIPPED...")
    print("starting main NOW..........")
    import main




