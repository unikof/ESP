import addr
import network
import espnow
import time
import machine

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes
#===================================================================
BUTTON_PIN = 2  # D2 corresponds to GPIO2 on ESP32

# Button press handler function
def button_handler(pin):
    print("Button pressed!")
    # Add your custom logic here

# Configure the button pin
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# Set up an interrupt for the button
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler)

# Configure wake-up from deep sleep on button press
machine.wake_on_ext0(pin=button, level=machine.Pin.WAKE_LOW)

# Check the reset cause
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("Woke up from deep sleep!")
else:
    print("Cold boot or other reset")

# Simulate some work before entering deep sleep
print("Waiting for button press...")
time.sleep(5)  # Simulate some delay to allow button press handling

# Enter deep sleep
print("Entering deep sleep...")
time.sleep(1)  # Small delay to ensure messages are printed

#machine.deepsleep()




"""
print("current MAC: ", get_espnow_mac())

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

msg = "Hello from ESP_2"
esp.add_peer(addr.detsk_light_potolok)

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
            return msg.decode()
    return "timeout"

send_mess("light_on", addr.detsk_light_potolok)
"""












print("end...")

