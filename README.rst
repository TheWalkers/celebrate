**BUILDING**

https://papersignals.withgoogle.com/getstarted#assemble-the-hardware

**CONFIGURE WIFI**

Download repo - https://github.com/TheWalkers/celebrate

Replace wifi credentials in robot/connect.py.

Install rshell - pip install rshell

$ rshell
> connect serial /dev/tty.SLAB_USBtoUART 115200
> cp path_to_code/celebrate/robot/* /pyboard/


**MicroPython REPL**

screen /dev/tty.SLAB_USBtoUART 115200
CTRL-A CTRL-\.

or...

$ rshell
> connect serial /dev/tty.SLAB_USBtoUART 115200
> cp path_to_code/celebrate/robot/* /pyboard/

**REFLASH**

pip install esptool

https://micropython.org/download/esp8266/

USB to UART drivers

https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers


# add to wheel group. not sure if necessary
sudo dscl . append /Groups/wheel GroupMembership gmackrill

esptool.py --port /dev/tty.SLAB_USBtoUART flash_id && esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash && esptool.py --port /dev/tty.SLAB_USBtoUART write_flash --flash_size=detect 0 ~/Downloads/esp8266-20220117-v1.18.bin 






