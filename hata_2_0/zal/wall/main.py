import network
import espnow
from time import sleep_ms, ticks_ms, ticks_diff
from addr import zal_light, get_espnow_mac
import machine
import gc

hyphens = "=" * 40 + ">>>"
ticks_check = ticks_ms()

button_floor = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
button_telik = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
button_divan = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
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
    #print(msg);return
    
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
def on_click(button_name):
    global reboot_factor
    
    if button_name == "floor":
        send_mess("floor_click")
    elif button_name == "telik":
        send_mess("telik_click")
    elif button_name == "divan":
        send_mess("divan_click")
        
    reboot_factor = 0

def on_long_press(button_name):
    global reboot_factor
    
    if button_name == "floor":
        send_mess("floor_long_press")
        reboot_factor += 1
        #print(reboot_factor)
        if reboot_factor > 5:
            device_reboot()
        
    elif button_name == "telik":
        send_mess("telik_long_press")
        
    elif button_name == "divan":
        send_mess("divan_long_press")
        
def button_pressed(button_name):
    current_time = ticks_ms()
    score = 0
    
    while ticks_diff(ticks_ms(), current_time) < 50:
        if button_name == "floor":
            if button_floor.value() == 0:
                score += 1
                
        elif button_name == "telik":    
            if button_telik.value() == 0:
                score += 1
                
        elif button_name == "divan":    
            if button_divan.value() == 0:
                score += 1           

    if score < 10:
        return False
    else:
        #print(score)
        return True
    
def press_control(button_name):
    current_time = ticks_ms()
    
    while True:
        if button_pressed(button_name) == False:
            on_click(button_name)
            #print(f"CLICK {button_name}")
            sleep_ms(100)
            break
        
        elif ticks_diff(ticks_ms(), current_time) > 500:
            on_long_press(button_name)
            #print(f"LONG_PRESS {button_name}")
            sleep_ms(1000)
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
    if button_floor.value() == 0:
        press_control("floor")
        
    elif button_telik.value() == 0:
        press_control("telik")
        
    elif button_divan.value() == 0:
        press_control("divan")
        
    if ticks_diff(ticks_ms(), ticks_check) > 3600000:
        print("mem & espNow refresh....")

        gc.collect()

        esp.active(False)
        wlan.active(False)
        sleep_ms(5)
        wlan.active(True)
        esp.active(True)
        esp.add_peer(destination)

        ticks_check = ticks_ms()
        print(hyphens)

print(hyphens)
print("MAIN END...")
print(hyphens)





