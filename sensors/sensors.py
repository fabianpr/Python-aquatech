try:
    import time
    import os
    import sys
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
    def set_pin(self, pin):
        if pin in self.pins_io:
            self._pin = pin

    #TODO: metodo checar sensor
    def check_sensor(self, pin):
        self.is_full = Check_sensor(self._pin)


class WaterPump:
    def __init__(self, is_active, pins_io):
        self._is_active = is_active
        self._pins_io = pins_io
        self._pin = None

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        if value in self._pins_io:
            self._pin = value
        else:
            raise ValueError(f'Selected pin {value} for the control is not correct')

    def activate_sw(self):
        if self._is_active is False:
            self._is_active = True

    def deactivate_sw(self):
        if self._is_active is True:
            self._is_active = False

class Check_sensor:
    def __init__(self, pin, state):
        self.pin = pin
        self.state = state

    def sensor_value(self, pin):
#TODO get value
        #state = get_value
        return True #state