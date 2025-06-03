import machine
import network
import espnow
from time import sleep, sleep_ms
from addr import zal_wall, get_espnow_mac

hyphens = "=" * 40 + ">>>"
#===================================================================
#Led control
floor_led = machine.PWM(machine.Pin(21), freq=10000)
telik_led = machine.PWM(machine.Pin(19), freq=10000)
divan_led = machine.PWM(machine.Pin(18), freq=10000)
#===================================================================
#Mandatory sleep and get them off...
sleep_ms(10)

floor_led.duty(0)
telik_led.duty(0)
divan_led.duty(0)
#===================================================================
# light statuses, can be: off / on / half
floor_status = "off" 
telik_status = "off"
divan_status = "off"
#===================================================================
print(f"{hyphens}")
print("              ZAL LIGHT")
print(f"{hyphens}")
#===================================================================
"""
while True:
    floor_led.duty(1023)
    print("floor_led_on")
    sleep(1)
    floor_led.duty(0)
    print("floor_led_off")
    sleep(1)

    telik_led.duty(1023)
    print("telik_led_on")
    sleep(1)
    telik_led.duty(0)
    print("telik_led_off")
    sleep(1)
    
    divan_led.duty(1023)
    print("divan_led_on")
    sleep(1)
    divan_led.duty(0)
    print("divan_led_off")
    sleep(1)
    
    print(hyphens)
"""

def device_reboot():
    device_reboot()
    divan_led.duty(0)
    sleep_ms(300)
    divan_led.duty(1023)
    sleep_ms(300)
    divan_led.duty(0)
    sleep_ms(300)
    divan_led.duty(1023)
    sleep_ms(300)
    divan_led.duty(0)
    sleep_ms(300)
    divan_led.duty(1023)
    sleep_ms(300)
    divan_led.duty(0)
    print("rebooting system...")
    
    machine.reset()

def control_dag(code):
    global floor_status, telik_status, divan_status
    response = ""
    
    if code == "floor_click":
        if floor_status == "off":
            floor_led.duty(1023)
            floor_status = "on"
        else:
            floor_led.duty(0)
            floor_status = "off"
        response = f"response_{code}"
    
    elif code == "telik_click":
        if telik_status == "off":
            telik_led.duty(1023)
            telik_status = "on"
        else:
            telik_led.duty(0)
            telik_status = "off"
        response = f"response_{code}"
        
    elif code == "divan_click":
        if divan_status == "off":
            divan_led.duty(1023)
            divan_status = "on"
        else:
            divan_led.duty(0)
            divan_status = "off"
        response = f"response_{code}"
        
    elif code == "floor_long_press":
        floor_led.duty(0)
        telik_led.duty(0)
        divan_led.duty(0)
        
        floor_status = "off"
        telik_status = "off"
        divan_status = "off"
        
        response = f"response_{code}"
        
    elif code == "telik_long_press":
        telik_led.duty(45)
        telik_status = "half"
        
        response = f"response_{code}"
        
    elif code == "divan_long_press":
        divan_led.duty(45)
        divan_status = "half"
        
        response = f"response_{code}"
    
    elif code == "reboot":
        device_reboot()
    
    else:        
        response = f"unknown_command_{code}"
    
    print(f"statuses <floor/telik/divan> = <{floor_status}/{telik_status}/{divan_status}>")    
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
        print(f"received <<<<=== {code}")
        response_code = control_dag(code)
        sleep_ms(10)
        esp.send(destination, response_code)
        print(f"sent ===>>> {response_code}")
        print(hyphens)
#===================================================================
print(hyphens)
print("MAIN END...")
print(hyphens)

