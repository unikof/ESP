import addr
import network
import espnow
import time
import machine

BUTTON_PIN = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)   # D2 на вашей плате соответствует GPIO2
LED_PIN = 2
led = machine.PWM(machine.Pin(LED_PIN))

led.duty(0)
light_status = "off"

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes

print("current MAC: ", get_espnow_mac())
#===================================================================
time.sleep(3)
#===================================================================
def turn_on():
    global light_status
    light_status = "on"
    led.duty(1023)
    print("______________________", light_status)
    time.sleep_ms(300)
    
def turn_off():
    global light_status
    light_status = "off"
    led.duty(0)
    print("______", light_status)
    time.sleep_ms(300)
    
def turn_half():
    global light_status
    light_status = "half"
    led.duty(100)
    print("______________", light_status)
    time.sleep_ms(300)

#BUTTON_PIN.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

print("Waiting for button events...")

def button_pressed():
    if BUTTON_PIN.value() == 0:
        return True
    else:
        return False
    
def button_not_pressed():
    if BUTTON_PIN.value() == 0:
        return False
    else:
        return True
    
while True:
    #current_time = 0
    #time_diff = 0
    
    if (button_not_pressed() and light_status == "off") or (button_pressed() and light_status in ("on", "half")):
        time.sleep_ms(50)
       
    elif button_pressed() and light_status != "on":
        turn_on()
    
    elif button_not_pressed() and light_status != "off":
        time.sleep_ms(200)
        if button_not_pressed():
            turn_off()
        else:
            turn_half()    

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



