def do_connect():
    import time
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Lake House Guest')
        time.sleep(5)
        if not sta_if.isconnected():
            print('network didn\'t seem to come up.')
    print('network config:', sta_if.ifconfig())
