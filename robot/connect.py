AUTH = ('Lake House Guest',) #, 'password' )

def do_connect():
    import time
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print(f'connecting to network {AUTH}...')
        sta_if.active(True)
        sta_if.connect(*AUTH)
        time.sleep(5)
        if not sta_if.isconnected():
            print('network didn\'t seem to come up.')
    print('network config:', sta_if.ifconfig())
