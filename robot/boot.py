# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc
import webrepl

webrepl.start()
gc.collect()

import connect
connect.do_connect()

import ntptime
ntptime.settime()

should_watch = True
import urequests
try:
    debug_req = urequests.get('http://ak-celebrate.s3-us-west-2.amazonaws.com/no_watch.html')
    if debug_req.status_code == 200:
        should_watch = False
except:
    pass

if should_watch:
    import celebrate
    celebrate.watch()

