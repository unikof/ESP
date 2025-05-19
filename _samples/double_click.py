import addr
import network
import espnow
import time
from machine import Pin

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes

print("current MAC: ", get_espnow_mac())
#===================================================================
sum_click = 0
timing = 0
flag = 0

time.sleep(5)
#===================================================================
def on_click():
    print("Single click detected!")

def on_double_click():
    print("Double click detected!")

def on_long_press():
    print("Long press detected!")

"""
# Функция-обработчик нажатия кнопки
def handle_interrupt(pin):
    global last_time
    current_time = time.ticks_ms()  # Текущее время в миллисекундах
    if time.ticks_diff(current_time, last_time) > 300:  # Проверяем, прошло ли 200 мс
        click()
        last_time = current_time  # Обновляем время последнего срабатывания
    else:
        print(time.ticks_diff(current_time, last_time))
"""
# Пин, к которому подключена кнопка
BUTTON_PIN = Pin(4, Pin.IN, Pin.PULL_UP)   # D2 на вашей плате соответствует GPIO2

#BUTTON_PIN.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

print("Waiting for button press...")
while True:
    if BUTTON_PIN.value() == 0:
        on_click()
        if flag == 0:
            timing = time.ticks_ms()
            flag = 1
        sum_click = sum_click + 1
        
    if time.ticks_diff(time.ticks_ms(), timing) > 300:
        print(sum_click)
        
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


