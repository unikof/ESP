import machine
import network
import espnow
import time
import addr

LED_1 = 4
LED_2 = 2

led_1 = machine.Pin(LED_1, machine.Pin.OUT)
led_2 = machine.Pin(LED_2, machine.Pin.OUT)
#led_3 = machine.Pin(LED_3, machine.Pin.OUT)

#===================================================================
time.sleep(3)

print("current MAC: ", addr.get_espnow_mac())

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

destination = addr.zal_stena
esp.add_peer(destination)

print("start:")

while True:
    #led_2.value(1)
    time.sleep_ms(5)
    led_2.value(0)
    time.sleep_ms(5)

"""
while True:
    if esp.any():
        peer, msg = esp.recv()
        print(f"Received: {msg.decode()} from {peer}")
        esp.send(destination, "confirmed")
        print("confirmation sent...")

print("end....")
"""
