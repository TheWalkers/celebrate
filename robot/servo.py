


#  define SERVO_PIN 14
#  // Servo Positions and Intent specific Numbers
#  define CENTER_POSITION 90

# // Celebrate
# define STRETCHBREAK_TIME_REACHED 0
# define STRETCHBREAK_NOT_YET 90

# https://docs.micropython.org/en/latest/library/pyb.Pin.html
# pyb.Pin.board.X1

#  s1 = Servo(1) # servo on position 1 (X1, VIN, GND)

import machine
import time

CENTER_POSITION = 90

CELEBRATE_NOT_YET = CENTER_POSITION
CELEBRATE_NOW = 0

SERVO_PIN = 14


class Servo:
    def __init__(self):
        # return pyb.Servo(pyb.Pin.board.X1)
        # return pyb.Servo(SERVO_POSITION)
        pin = machine.Pin(SERVO_PIN)
        self.pwm = machine.PWM(pin, freq=50)
        self.position = 90

    def move_to(self, target_pos):
        # We set the duty cycle to 20  to position servo at 9 degree.
        # duty 70 –>  90 degree
        # duty 120 – > 180 degree
        duties = {9: 20,
                  90: 70,
                  180: 120
                  }
        target_duty = duties[target_pos]
        initial_duty = self.position
        for pos in range(initial_duty, target_duty, -1 if initial_duty > target_duty else 1):
            print(pos)
            self.pwm.duty(pos)
            time.sleep(.1)
        self.position = target_duty
