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

print("current MAC: ", get_espnow_mac())
#===================================================================
time.sleep(3)

sum_click = 0
timing = 0
flag = 0
#===================================================================
def on_click():
    print("Single click detected!")

def on_double_click():
    print("Double click detected!")

def on_long_press():
    print("Long press detected!")

BUTTON_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)   # D2 на вашей плате соответствует GPIO2

#BUTTON_PIN.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

def button_scan():
    global sum_click, timing, flag
    while True:
        if BUTTON_PIN.value() == 0:
            sum_click = sum_click + 1
            
            if flag == 0:
                timing = time.ticks_ms()
                flag = 1
      
        if time.ticks_diff(time.ticks_ms(), timing) > 500 and flag == 1:
            print(sum_click)
            if sum_click <= 8000:
                print(sum_click)
                on_click()
                flag = 0
                sum_click = 0
                time.sleep_ms(500)
                break
            elif sum_click >= 8000:
                print(sum_click)
                on_long_press()
                flag = 0
                sum_click = 0
                time.sleep_ms(1000)
                break
            else:
                flag = 0
                sum_click = 0
                break
    machine.deepsleep()
                
def handle_interrupt(pin):
    button_scan()

BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
machine.wake_on_ext0(pin=BUTTON_PIN, level=machine.Pin.WAKE_LOW)

print("Waiting for button events...")

#machine.deepsleep()

"""
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


