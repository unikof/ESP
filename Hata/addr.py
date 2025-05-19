import network

zal_stena = b'\xC0\x5D\x89\xB0\x9C\xB8'
zal_light = b'\x34\x5F\x45\xAA\x48\xAC'

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes