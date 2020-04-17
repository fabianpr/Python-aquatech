from log import log
from sensors import *
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

ledPin = 13
ledState = False


class core():
    try:
        connection = SerialManager(device='/dev/ttyACM0')
        ard = ArduinoApi(connection = connection)
    except:
        print("Fallo en Conexion Arduino")


    def fill_refugim(self):
        try:
            while refugim_water_level is False:
                valve.open()
        except Exception as e:
            log.error("Error en sensor proceso para llenar a nivel el almacer de agua.")
            print(e)

    def wave_maker(self):
        if return_pump is True:
            pump_sequence = [10, 7]
        else:
            pump_sequence = [90, 7]
        wave_rele.activate(pump_sequence)

    def return_pump_proc(self):
        if day_cycle.activated():
            pump_rele.day_poc()
        elif day_cycle.sleep():
            pump_rele.sleep_proc()
        elif clean_cycle.dump():
            pump_rele.clean()
        elif clean_cycle.fill():
            pump_rele.fill()
        else:
            pass

    def uv_light(self):
        if water_flow.high():
            uv_rele.active()
        else:
            uv_rele.deactivate()

    def feeding_cycle(self):
        if day_cycle.activated():
            pump_rele.stop()
        else:
            wave_maker()

class night_cycle():
    active = 0
    def activated(self):
        active = 1
        return True

    def deactivate():
        active = 0
        return True

    def check_time():
        return

class day_cycle():
    active = 0
    def activate(self):
        active = 1
        check_time()
        return True

    def deactivate():
        active = 0
        check_time()
        return True

    def check_time():
        return

