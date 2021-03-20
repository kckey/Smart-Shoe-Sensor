import board
import busio
import time
import csv
#walk test slow 
i2c=busio.I2C(board.SCL,board.SDA)

import adafruit_ads1x15.ads1015 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c, address=0x48)

heel = AnalogIn(ads,ADS.P0)
toe = AnalogIn(ads,ADS.P1)
i=0

f = open("walk_Data[slow].csv","w", newline="")
c=csv.writer(f)

start_time = time.time()
seconds = 25

heelPhase = 0
toePhase = 0
c.writerow(["Heel Value","Heel Phase","Toe Value","Toe Phase","Time"])
while True:
	current_time = time.time()
	elapsed_time = current_time - start_time
	print("heel:",heel.value,heel.voltage, heelPhase," | toe:",toe.value,toe.voltage,toePhase)
	print("   ")
	time.sleep(.001)

	if heel.value > 30000:
	    heelPhase = 1
	else:
	    heelPhase = 0
	if toe.value > 20000:
	    toePhase = 1
	else:
	    toePhase = 0
	c.writerow([heel.value, heelPhase, toe.value, toePhase, elapsed_time])
	if elapsed_time > seconds:
	    print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
	    break

