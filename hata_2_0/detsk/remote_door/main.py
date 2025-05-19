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

destination = b'\xC0\x5D\x89\xB0\x9C\xB8'

#b'\x34\x5F\x45\xAA\x48\xAC'
#b'\xC0\x5D\x89\xB0\x9C\xB8'

msg = "Hello from ESP_2"
esp.add_peer(destination)

def send_mess(msg, dest):
    for x in range(10):
        esp.send(dest, msg)
        print(f"Sent: {msg} -> {dest}")
        response = wait_for_response()
        if response == "confirmed":
            print("confirmed on: ", x)
            return
    print("timeout...(((")    
    
def wait_for_response(timeout_ms = 100):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < timeout_ms:
        if esp.any():
            peer, msg = esp.recv()
            print(f"Received: {msg.decode()} from {peer}")
            return msg
    return "timeout"

send_mess("aaaaa", destination)

print("end....")

