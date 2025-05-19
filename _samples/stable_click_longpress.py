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
time.sleep(4)
#===================================================================
def on_click():
    print("Single click detected!")
    led.value(1)  # Включаем светодиод
    time.sleep_ms(100)
    led.value(0)

def on_long_press():
    print("Long press detected!")
    led.value(1)  # Включаем светодиод
    time.sleep_ms(1000)
    led.value(0)

BUTTON_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)   # D2 на вашей плате соответствует GPIO2
LED_PIN = 2
led = machine.Pin(LED_PIN, machine.Pin.OUT)  # Настраиваем пин как выход

#BUTTON_PIN.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

print("Waiting for button events...")

def button_pressed():
    if BUTTON_PIN.value() == 0:
        return True
    else:
        return False
    
while True:
    current_time = 0
    time_diff = 0
    
    if button_pressed() == True:
        time.sleep_ms(30)
        current_time = time.ticks_ms()
        
        while True:
            time_diff = time.ticks_diff(time.ticks_ms(), current_time)
            if button_pressed() == False or time_diff >= 400:
                if time_diff >= 400:
                    print(time_diff)
                    on_long_press() 
                    current_time = 0
                    time_diff = 0
                    break
                else:
                    print(time_diff)
                    on_click()
                    current_time = 0
                    time_diff = 0
                    break
                
#def handle_interrupt(pin):
#    button_scan()

#BUTTON_PIN.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)




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



