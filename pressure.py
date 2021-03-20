import board
import busio
import time
i2c=busio.I2C(board.SCL,board.SDA)

import adafruit_ads1x15.ads1015 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c, address=0x48)

chan = AnalogIn(ads,ADS.P0)
ghan = AnalogIn(ads,ADS.P1)
i=0
while i<=10:
	print("heel:",chan.value,chan.voltage," | toe:",ghan.value,ghan.voltage)
	print("   ")
	time.sleep(.01)
