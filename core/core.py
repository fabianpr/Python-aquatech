from log import *
from sensors import sensors
from nanpy import (ArduinoApi, SerialManager, Lcd)
from time import sleep
from datetime import datetime
import sys

sys.path.append(".")
#from display import *
#from display import Lcd_display

ledPin = 13
ledState = False
pins = [7, 8, 9, 10, 11, 12]
cols, rows = 16, 2
#lcd = Lcd(pins, [cols, rows]) descomentar o cambiar


def check_temp(temp):
    valor_temp = temp.sensor_value()
    """Convert value to Celcius"""
    return 0.0


class Core(sensors.Control):
    def __init__(self):
        try:
            connection = SerialManager(device='/dev/ttyACM0') # TODO script bash y variable
            ard = ArduinoApi(connection=connection)
            #lcd.setCursor(0,0)
            #Lcd_display.write_lcd(connection,"Conectado Ard:Pi")
        except:
            #Lcd_display.write_lcd(connection,"Err Conn Arduino")
            print('error')
            # TODO: FLAG TO RESTART /SEARCH ARDUINO
        self.water_pump = sensors.Control(False, 8, ard)
        self.uv_light = sensors.Control(False, 9, ard)
        self.heater = sensors.Control(False, 10, ard)
        self.rwater_level = sensors.Control(False, 11, ard)
        self.rwater_fill = sensors.Control(False, 12, ard)
        self.wave_maker = sensors.Control(False, 13, ard)
        self.uv_rele = sensors.Control(False, 7, ard)
        self.water_flow = sensors.Control(False, 6, ard)
        self.temp = sensors.Check_Sensor(5, "state")


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

    def uv_light(self, water_flow, uv_rele):
        if water_flow.sensor_value() :
            uv_rele.activate_sw()
        else:
            uv_rele.deactivate_sw()

    def DayCycle(self, temp, activate, water_pump, wave_maker, sunset=False):

        if activate is True and sunset is False:
            water_pump.activate_sw()
            log.event("Event: Day Cycle is activated")
            if sunset is False:
                # TODO get temp
                temp_val = check_temp(temp)
                log.registry("Day Cycle", temp_val, 1, 1)
                water_pump.deactivate_sw()
                wave_maker.activate_sw()
                return False
        return True

    ###Borrar?
    def deactivate(self, sunset):
        water_pump.deactivate_sw()
        sunset if Core.check_time().time() > datetime.strptime('08:00', '%H:%M').time() else False
        if sunset is True:

            water_pump.activate_sw()
            return False

    def NightCycle(self, activate, water_pump, sunset=False):
        water_pump.deactivate_sw()
        log.event("Event: Night Cycle is activated")
        if activate is True and sunset is True:
            water_pump.deactivate_sw()
            if sunset is True:
                # TODO get temp
                temp_val = check_temp(temp)
                log.registry("Night Cycle", temp_val, 0, 0)
                water_pump.deactivate_sw()
                return False
        return True





class Waves:
    def activate(self, wave_maker):
        wave_maker.activate_sw()
