import machine
import network
import espnow
from time import sleep, sleep_ms
import addr

hyphens = "=" * 40 + ">>>"

#LED_1 = 1
LED_2 = 2
#LED_3 = 3

#pwm_led_1 = machine.PWM(machine.Pin(LED_1), freq=1000)
pwm_led_2 = machine.PWM(machine.Pin(LED_2), freq=1000)
#pwm_led_3 = machine.PWM(machine.Pin(LED_3), freq=1000)

#pwm_led_1.duty(0)
pwm_led_2.duty(0)
#pwm_led_3.duty(0)

commands = ["floor_click", "floor_longpress", "telik_click", "telik_longpress", "divan_click", "divan_longpress"]

lights = {
  "floor": 0,
  "telik": 0,
  "divan": 0
}
#===================================================================
print(f"{hyphens}     ZAL LIGHT   ")
#===================================================================
def control_dag(code):
    if code in commands:
        response = f"response_{code}"
        
        #ligh control logic
        
    else:
        response = f"unknown_command_{code}"
   
        
    return response
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

while True:
    if esp.any():
        peer, msg = esp.recv()
        code = msg.decode()
        print(f"received <<<<=== {code}")
        #response_code = control_dag(code)
        response_code = f"response_{code}"
        sleep_ms(10)
        esp.send(destination, response_code)
        print(f"sent ===>>> {response_code}")
        print(hyphens)
"""
while True:
    pwm_led_2.duty(0)
    sleep_ms(1000)
    pwm_led_2.duty(1023)
    sleep_ms(1000)
    
while True:
    for duty in range(0, 50, 1):
        print(duty)
        pwm_led_2.duty(duty)
        sleep_ms(500)
"""






print(hyphens)
print("MAIN END...")
print(hyphens)


