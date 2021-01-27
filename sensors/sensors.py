try:
    import time
    import os
    import sys
    import RPi.GPIO as GPIO
except Exception as e:
    print("Error in Python modules, maybe missing: {}".format(e))



class Light:
    def __init__(self, state, value):
        self.state = state
        self.value = value


class Refugim_water_level:
    def __init__(self, is_full, pins_io):
        self._is_full = is_full
        self._pins_io = pins_io
        self._pin = None

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        if value in self._pins_io:
            self._pin = value
            GPIO.setup(self._pin, GPIO.IN)
            GPIO.output(self._pin, GPIO.LOW)
            self._ard.pinMode(self._pin, self._ard.OUTPUT)
            self._ard.digitalWrite(self._pin, self._ard.LOW)
        else:
            raise ValueError(f'Selected pin {value} for {self.__class__.__name__} control is not correct')

    #TODO: metodo checar sensor
    def check_sensor(self, pin):
        self.is_full = Check_Sensor(self._pin)


class Control:
    def __init__(self, is_active, pins_io, arduino):
        self._is_active = is_active
        self._pins_io = pins_io
        self._pin = None
        self._ard = arduino
        #GPIO.setmode(GPIO.BCM)

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        if value in self._pins_io:
            self._pin = value
            GPIO.setup(self._pin, GPIO.OUT)
            GPIO.output(self._pin, GPIO.LOW)
            self._ard.pinMode(self._pin, self._ard.OUTPUT)
            self._ard.digitalWrite(self._pin, self._ard.LOW)
        else:
            raise ValueError(f'Selected pin {value} for {self.__class__.__name__} control is not correct')

    def activate_sw(self):
        if self._is_active is False:
            self._is_active = True
            self._ard.digitalWrite(self._pin, self._ard.HIGH)

    def deactivate_sw(self):
        if self._is_active is True:
            self._is_active = False
            self._ard.digitalWrite(self._pin, self._ard.LOW)


class Check_Sensor:
    def __init__(self, pin, state):
        self.pin = pin
        self.state = state

    def sensor_value(self, pin):
#TODO get value
        #state = get_value
        return True #state
