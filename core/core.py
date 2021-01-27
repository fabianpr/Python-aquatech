import log
from sensors import *
from nanpy import (ArduinoApi, SerialManager, Lcd)
from time import sleep
from datetime import datetime

sys.path.append(".")
#from display import *
#from display import Lcd_display

ledPin = 13
ledState = False
pins = [7, 8, 9, 10, 11, 12]
cols, rows = 16, 2
#lcd = Lcd(pins, [cols, rows]) descomentar o cambiar


water_pump = sensors.Control(False, 1000, '')
uv_light = sensors.Control(False, 1001, '')
heater = sensors.Control(False, 1002, '')
rwater_level = sensors.Control(False, 1003, '')
rwater_fill = sensors.Control(False, 1004, '')
wave_maker = sensors.Control(False, 1005, '')

class Core:
    def __init__(self):
        try:
            connection = SerialManager(device='/dev/ttyACM0') # TODO script bash y variable
            ard = ArduinoApi(connection = connection)
            #lcd.setCursor(0,0)
            #Lcd_display.write_lcd(connection,"Conectado Ard:Pi")
        except:
            #Lcd_display.write_lcd(connection,"Err Conn Arduino")
            print('error')
            # TODO: FLAG TO RESTART /SEARCH ARDUINO

    def check_time(self):
        return datetime.time()

    def fill_refugim(self, rwater_level, rwater_fill):
        try:
            while rwater_level.is_active is False:
                rwater_fill.activate_sw()
        except Exception as e:
            log.event("Error: en sensor proceso para llenar a nivel el almacen de agua.")
            print(e)

    def wave_maker(self, water_pump, waves):
        if water_pump.is_active is True:
            pump_sequence = [10, 7]
        else:
            pump_sequence = [90, 7]
        waves.activate(pump_sequence)

    def return_pump_proc(self):
        if DayCycle.activated():
            pump_rele.day_poc()
        elif DayCycle.sleep():
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
        if DayCycle.activated():
            pump_rele.stop()
        else:
            wave_maker()


class NightCycle(Core):
    def __init__(self):
        self.morning = False

    def activated(self, morning):
        morning if Core.check_time().time() > datetime.strptime('08:00', '%H:%M').time() else False
        return True

    def deactivate(self, morning):
        morning if Core.check_time().time() > datetime.strptime('08:00', '%H:%M').time() else False
        return True


class DayCycle(Core):
    def __init__(self):
        self.sunset = False

    def activate(self, sunset):
        water_pump.activate_sw()
        sunset if Core.check_time().time() > datetime.strptime('08:00', '%H:%M').time() else False
        print(sunset)
        if sunset is True:
            water_pump.deactivate_sw()
            return False
        return True

    def deactivate(self, sunset):
        water_pump.deactivate_sw()
        sunset if Core.check_time().time() > datetime.strptime('08:00', '%H:%M').time() else False
        if sunset is False:
            water_pump.activate_sw()
            return False
        return True


class Waves:
    def activate(self, wave_maker):
        wave_maker.activate_sw()

cy = DayCycle()
print(cy.activate(False))