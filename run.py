from log import *
from core.core import Core
from datetime import datetime


def check_time(run):
    if run.check_time().time() < datetime.strptime('08:00', '%H:%M').time():
        sunset = False
    else:
        sunset = True
    return sunset

def day_cycle(run, sunset):
    if sunset is False:
        run.DayCycle()
    else:
        run.NightCycle()
        return False
    return True

def feeding_cycle(self, run):
    if day_cycle is True:
        run.pump_rele(False)
    else:
        print()
        #TODO marca de hora para ciclo de lipieza wave_maker()

def main():
    log.event("START RUN")
    run = Core()
    sunset = False
    sunset = check_time(run)
    day_cycle(run, sunset)

