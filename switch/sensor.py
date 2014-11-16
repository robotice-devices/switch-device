#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO

def get_data(sensor):
    """
    """

    port = sensor.get('port')
    GPIO.setup(port, GPIO.IN)
    state = GPIO.input(port)

    data = []
    data.append(("%s.switch" % sensor.get('name'), state))
      
    return data