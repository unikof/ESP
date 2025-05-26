import machine
import network
import espnow
from time import sleep, sleep_ms
import addr

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
telik_staus = "off"
divan_staus = "off"
#===================================================================
print(f"{hyphens}     ZAL LIGHT   ")
#===================================================================
def control_dag(code):
    if code == "floor_click":
        if floor_status == "off":
            floor_led.duty(1023)
            floor_status = "on"
        else:
            floor_led.duty(0)
            floor_status = "off"
        return f"response_{code}"
    
    elif code == "telik_click":
        if telik_staus == "off":
            telik_led.duty(1023)
            telik_staus = "on"
        else:
            telik_led.duty(0)
            telik_staus = "off"
        return f"response_{code}"
        
    elif code == "divan_click":
        if divan_staus == "off":
            divan_led.duty(1023)
            divan_staus = "on"
        else:
            divan_led.duty(0)
            divan_staus = "off"
        return f"response_{code}"
    
    else:
        return f"unknown_command_{code}"
#===================================================================
#print("current MAC: ", addr.get_espnow_mac())
print("standing up WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

destination = addr.zal_wall
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


