import network

zal_wall = b'\xC0\x5D\x89\xB0\x9C\xB8'
zal_light = b'\x14\x33\x5C\x53\x65\xE0'

def get_espnow_mac():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac = wlan.config('mac')
    
    mac_bytes = "b'" + "".join(f"\\x{b:02X}" for b in mac) + "'"
    return mac_bytes
