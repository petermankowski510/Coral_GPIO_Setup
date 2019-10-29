# Toggle LED through GPIO function
# Author: Peter Mankowski

from periphery import GPIO
import time

# GPIO init
gpio = GPIO(138, "low")

# Parameters declarations
count = 0
How_many_counts = 4
sleep_del = 0.1

"""
gpio.write(True)
time.sleep(1)
"""
# Toggle GPIO feature
while (count < How_many_counts):
    count = count + 1
    value = gpio.read()
    gpio.write(not value)
    time.sleep(sleep_del)

gpio.close()