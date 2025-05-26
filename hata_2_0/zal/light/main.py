import machine
import network
import espnow
from time import sleep, sleep_ms
from addr import zal_wall

hyphens = "=" * 40 + ">>>"
#===================================================================
#Led control
floor_led = machine.PWM(machine.Pin(18), freq=10000)
telik_led = machine.PWM(machine.Pin(19), freq=10000)
divan_led = machine.PWM(machine.Pin(21), freq=10000)

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
    
    else:        
        response = f"unknown_command_{code}"
    
    print(f"statuses <floor/telik/divan> = <{floor_status}/{telik_status}/{divan_status}>")    
    return response

#===================================================================
#print("current MAC: ", addr.get_espnow_mac())
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
"""
while True:
    telik_led.duty(1023)
    sleep_ms(1000)
    telik_led.duty(0)
    sleep_ms(1000)       



while True:
    for duty in range(30, 100, 3):
        print(duty)
        floor_led.duty(duty)
        telik_led.duty(duty)
        divan_led.duty(duty)
        sleep_ms(500)
"""


