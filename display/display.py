#from RPLCD import CharLCD
import time

#lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
## lcd.write_string(u'Hello world!')

#class pantalla:
#    def escribe(self,texto):
#        self.texto = texto
#        write_to_lcd(lcd, framebuffer, 16)
#        if len(texto) > 16:
#            for k in range(0,2):
#                loop_string(texto, lcd, framebuffer, 1, 16)
#        else:
#            lcd.write_string(texto.decode('unicode-escape'))


#framebuffer = [
#    '',
#    '',
#] 

#def write_to_lcd(lcd, framebuffer, num_cols):
#    lcd.home()
#    for row in framebuffer:
#        lcd.write_string(row.ljust(num_cols)[:num_cols])
#        lcd.write_string('\r\n')

#def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.3): #DELAY= CONTROLS THE SPEED OF SCROLL
#    padding = ' ' * num_cols
#    s = padding + string + padding
#    for i in range(len(s) - num_cols + 1):
#        framebuffer[row] = s[i:i+num_cols]
#        write_to_lcd(lcd, framebuffer, num_cols)
#        time.sleep(delay)

# while True:
#     loop_string(long_string, lcd, framebuffer, 1, 16)

from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod


class Lcd_display():
    cols, rows = 16, 2
    pins = [2,3,4,5,6,7]
    lcd = Lcd(pins, [cols,rows], connection = connection)

    def write_lcd(self,connection, message):
        self.message = message
        lcd.clear()
        if len(message) > 16:
            lcd.setCursor(16,1)
            lcd.autoscroll()
            for char in message:
                lcd.printString(char.decode('unicode-escape'))
                time.sleep(0.37)
        else:
            lcd.setCursor(0,0)
            lcd.printString(char.decode('unicode-escape'))
            