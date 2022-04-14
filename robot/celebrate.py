import time

try:
    import urequests
except:
    # debugging
    import requests as urequests

import servo

WAIT_TIME = 5 * 60
WAIT_TIME = 5
SERVO = servo.Servo()

# don't do redirects or tls
BASE_URL = 'http://ak-celebrate.s3-us-west-2.amazonaws.com/'


def arms_up():
    print('arms up!')
    SERVO.move_to(90)


def arms_down():
    print('arms down')
    SERVO.move_to(180)


def celebrate():
    print('start celebrating')
    arms_up()
    # hold for 5 seconds
    arms_down()


def prev_time_mask():
    # micropython doesn't have datetime
    
    # dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H')

    now = time.gmtime()
    dt = f'{now[0]}-{now[1]}-{now[2]}-{now[3]}'
    minute_mask = now[4] // 5
    # minute_mask = int(datetime.datetime.utcnow().strftime('%M')) // 5
    if minute_mask == 0:
        previous_minute_mask = 11
    else:
        previous_minute_mask = minute_mask - 1
    return f'{dt}_{str(previous_minute_mask)}'


def watch():
    while True:
        url = f'{BASE_URL}{prev_time_mask()}.html'
        print(url)
        # url = 'https://roboticdogs.actionkit.com'
        try:
            resp = urequests.get(url)
            if resp.status_code != 200:
                print(f'Status code {resp.status_code} instead of 200')
            else:
                print('success!')
                celebrate()
        except:
            print('no luck, let\'s wait and then try again.')
        time.sleep(WAIT_TIME)

if __name__ == '__main__':
    watch()
