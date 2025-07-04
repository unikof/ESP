import machine
import network
import espnow
from time import sleep, sleep_ms, ticks_ms, ticks_diff
from addr import korr_wall, get_espnow_mac
import gc

hyphens = "=" * 40 + ">>>"
refresh_factor = 0
#===================================================================
#Led control
floor_led = machine.PWM(machine.Pin(21), freq = 10000)

radio_1 = machine.Pin(25, machine.Pin.IN)
radio_2 = machine.Pin(14, machine.Pin.IN)
radio_3 = machine.Pin(27, machine.Pin.IN)
radio_4 = machine.Pin(26, machine.Pin.IN)#, machine.Pin.PULL_UP)

cycle_light_levels = [10, 40, 100, 400, 1023]
current_level = 0
#===================================================================
#Mandatory sleep and get them off...
sleep_ms(10)
rtc = machine.RTC()
floor_led.duty(0)
#===================================================================
print(f"{hyphens}")
print("              KORRIDOR LIGHT")
print(f"{hyphens}")
#===================================================================
# Check:
"""
while True:
    floor_led.duty(50)
    print("floor_led_on")
    sleep(1)
    floor_led.duty(0)
    print("floor_led_off")

    telik_led.duty(100)
    print("telik_led_on")
    sleep(1)
    telik_led.duty(0)
    print("telik_led_off")
    
    divan_led.duty(150)
    print("divan_led_on")
    sleep(1)
    divan_led.duty(0)
    print("divan_led_off")
    
    print(hyphens)
"""
#===================================================================
def device_reboot():
    for _ in range(5):
        floor_led.duty(half_light_level)
        led_sleep(300)
        floor_led.duty(0)
        led_sleep(300)
        
    print("rebooting system...")
    rtc.memory(b'yes')
    machine.reset()
    
def refresh_status():
    global refresh_factor
    
    refresh_factor += 1
    
    if refresh_factor > 100:
        print(hyphens)
        print("mem & espNow refresh....")
        gc.collect()
        esp.active(False)
        wlan.active(False)
        led_sleep(5)
        wlan.active(True)
        esp.active(True)
        esp.add_peer(zal_wall)
        refresh_factor = 0
        print(hyphens)

def led_sleep(ms):
    check_led.duty(full_light_level)
    sleep_ms(ms)
    check_led.duty(0)
    
def show_statuses():
    print(f"statuses: ===>                                floor ===> {floor_status}  level ===> ")
#===================================================================
def floor_dag():
    global floor_status
    if floor_status == "off":
        floor_led.duty(full_light_level)
        floor_status = "on"
    else:
        floor_led.duty(0)
        floor_status = "off"
    show_statuses()
        
def floor_long_dag():
    global floor_status, telik_status, divan_status
    floor_led.duty(0)
    telik_led.duty(0)
    divan_led.duty(0)

    floor_status = "off"
    telik_status = "off"
    divan_status = "off"
    
    show_statuses()
#===================================================================
def esp_now_mess_received(code):    
    response = ""
    
    if code == "floor_click":
        floor_dag()
        response = f"response_{code}"
    
    elif code == "floor_long_press":
        floor_long_dag()
        response = f"response_{code}"
            
    elif code == "reboot":
        device_reboot()
    
    else:        
        response = f"unknown_command_{code}"
    
    return response

#===================================================================
print("current MAC: ", get_espnow_mac())
print("standing up WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

destination = zal_wall
esp.add_peer(destination)

print("receiving...:")
print(hyphens)
#===================================================================
while True:
    if esp.any():
        peer, msg = esp.recv()
        code = msg.decode()
        #print(f"received <<<<=== {code}")
        response_code = esp_now_mess_received(code)
        led_sleep(10)
        esp.send(destination, response_code)
        #print(f"sent ===>>> {response_code}")
        refresh_status()
        print(hyphens)
    
    elif radio_1.value() == 1:
        floor_dag()
        led_sleep(200)
        
    elif radio_2.value() == 1:
        telik_dag()
        led_sleep(200)
        
    elif radio_3.value() == 1:
        divan_dag()
        led_sleep(200)
    
    elif radio_4.value() == 1:
        pass
    
    #print(radio_1.value())
    #print(radio_2.value())
    #print(radio_3.value())
    #print(radio_4.value())
#===================================================================
print(hyphens)
print("MAIN END...")
print(hyphens)


