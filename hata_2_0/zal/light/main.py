import machine
import network
import espnow
import time
import addr

LED_1 = 4
LED_2 = 2

led_1 = machine.Pin(LED_1, machine.Pin.OUT)
#led_2 = machine.Pin(LED_2, machine.Pin.OUT)
#led_3 = machine.Pin(LED_3, machine.Pin.OUT)

pwm_led_2 = machine.PWM(machine.Pin(LED_2), freq=1000)
pwm_led_2.duty(0)

#===================================================================
time.sleep(1)

print("current MAC: ", addr.get_espnow_mac())

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

destination = addr.zal_wall
esp.add_peer(destination)

print("start:")

while True:
    pwm_led_2.duty(0)
    time.sleep_ms(1000)
    pwm_led_2.duty(1023)
    time.sleep_ms(1000)

"""
while True:
    for duty in range(0, 50, 1):
        print(duty)
        pwm_led_2.duty(duty)
        time.sleep_ms(500)






while True:
    if esp.any():
        peer, msg = esp.recv()
        print(f"Received: {msg.decode()} from {peer}")
        esp.send(destination, "confirmed")
        print("confirmation sent...")

print("end....")
"""

