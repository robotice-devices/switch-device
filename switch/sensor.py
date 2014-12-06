
try:
    import Adafruit_BBIO.GPIO as GPIO
    device = 'bbb'
except Exception, e:
    pass

try:
    import RPi.GPIO as GPIO
    device = 'rpi'
except Exception, e:
    pass

def get_data(sensor):
    """
    Switch status reading
    """
    data = []

    port = sensor['port']
    GPIO.setup(port, GPIO.IN)
    state = GPIO.input(port)

    data.append(("%s.switch" % sensor.get('name'), state))
      
    return data