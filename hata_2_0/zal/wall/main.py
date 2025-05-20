import network
import espnow
from time import sleep, sleep_ms, ticks_ms, ticks_diff
from addr import zal_light

hyphens = "=" * 40 + ">>>"
#===================================================================
print(f"{hyphens}     ZAL WALL   ")
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
#print("current MAC: ", addr.get_espnow_mac())
print("standing up WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

esp.add_peer(zal_light)

print("listening butts...:")
print(hyphens)
   
send_mess("aaaaa")
sleep(1)
send_mess("bbbb")

sleep(1)
send_mess("zzz")

sleep(1)
send_mess("fff")

sleep(1)
send_mess("ggg")

sleep(1)
send_mess("hhh")

sleep(1)
send_mess("jjj")

sleep(1)
send_mess("kkk")

print(hyphens)
print("MAIN END...")
print(hyphens)
