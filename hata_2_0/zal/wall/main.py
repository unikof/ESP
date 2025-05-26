import network
import espnow
from time import sleep, sleep_ms, ticks_ms, ticks_diff
from addr import zal_light, get_espnow_mac
import machine

hyphens = "=" * 40 + ">>>"
#===================================================================
print(f"{hyphens}")
print("              ZAL WALL")
print(f"{hyphens}")
#===================================================================
def send_mess(msg):
    for x in range(5):
        esp.send(zal_light, msg)
        print(f"request ===>>> {msg}")
        response = wait_for_response()
        print(f"response <<<=== {response} >>{x}th try<<<")
        if response != "TIME_OUT":
            return

def wait_for_response():
    start_timing = ticks_ms()
    while ticks_diff(ticks_ms(), start_timing) < 100: # 100ms timeout
        if esp.any():
            peer, msg = esp.recv()
            return msg.decode()
    return "TIME_OUT"
#===================================================================
print("current MAC: ", get_espnow_mac())
print("standing up WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

esp.add_peer(zal_light)

print("listening butts...:")
print(hyphens)
   
send_mess("telik_click")
sleep(1)
send_mess("telik_click")
sleep(1)
send_mess("telik_click")
sleep(1)
send_mess("telik_click")
sleep(1)
send_mess("telik_click")
sleep(1)
send_mess("telik_click")
sleep(1)


print(hyphens)
print("MAIN END...")
print(hyphens)

