import network
import espnow
from time import sleep_ms, ticks_ms, ticks_diff
from addr import zal_light, get_espnow_mac
import machine

hyphens = "=" * 40 + ">>>"
button_1 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
button_2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
button_3 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
#===================================================================
print(f"{hyphens}")
print("              ZAL WALL")
print(f"{hyphens}")

reboot_factor = 0
#===================================================================
def device_reboot():
    print(hyphens)
    print("reboot..")
    send_mess("reboot")
    machine.reset()

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
def on_click(button_number):
    global reboot_factor
    
    if button_number == 1:
        send_mess("floor_click")
    if button_number == 2:
        send_mess("telik_click")
    if button_number == 3:
        send_mess("divan_click")
        
    reboot_factor = 0
    sleep_ms(500)

def on_long_press(button_number):
    global reboot_factor
    
    if button_number == 1:
        send_mess("floor_long_press")
        reboot_factor +=1
        if reboot_factor > 10:
            device_reboot()
        
    if button_number == 2:
        send_mess("telik_long_press")
        
    if button_number == 3:
        send_mess("divan_long_press")
    
    sleep_ms(1000)

def button_pressed(button):
    if button.value() == 0:
        return True
    else:
        return False

def get_press_type(button, numb):
    sleep_ms(50) #Tremor
    current_time = ticks_ms()
    time_diff = 0
    
    while True:
        time_diff = ticks_diff(ticks_ms(), current_time)
        if button_pressed(button_1) == False or time_diff >= 500:
            if time_diff >= 500:
                #print(time_diff)
                on_long_press(numb)
                current_time = 0
                time_diff = 0
                break
            else:
                #print(time_diff)
                on_click(numb)
                current_time = 0
                time_diff = 0
                break
#===================================================================
print("current MAC: ", get_espnow_mac())
print("standing up WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

esp.add_peer(zal_light)

print("STARTED, listening butts...:")
print(hyphens)
    
   
while True:
    if button_pressed(button_1) == True:
        get_press_type(button_1, 1)
    
    if button_pressed(button_2) == True:
        get_press_type(button_2, 2)
    
    if button_pressed(button_3) == True:
        get_press_type(button_3, 3)
        
                    
"""

sleep(1)
send_mess("telik_click")
sleep(1)
"""

print(hyphens)
print("MAIN END...")
print(hyphens)


