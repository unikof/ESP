import network
import espnow
import time

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes
#===================================================================

print("current MAC: ", get_espnow_mac())

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

destination = b'\x34\x5F\x45\xAA\x48\xAC'

#b'\x34\x5F\x45\xAA\x48\xAC'
#b'\xC0\x5D\x89\xB0\x9C\xB8'

esp.add_peer(destination)

while True:
    if esp.any():
        peer, msg = esp.recv()
        print(f"Received: {msg.decode()} from {peer}")
        esp.send(destination, "confirmed")
        print("confirmation sent...")

print("end....")


