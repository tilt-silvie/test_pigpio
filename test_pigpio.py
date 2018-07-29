#!/usr/bin/env python

import time
import pigpio

pi = pigpio.pi()

if not pi.connected:
    exit(0)

# for LIS3DH acceleration sensor
ADDRESS = 0x19
REGISTER = 0x0f

i2c = pi.i2c_open(1, ADDRESS)

for i in range(100):
    print("printed. no." + str(i))
    data = pi.i2c_read_byte_data(i2c, REGISTER)
    print("recv:" + str(data))
    time.sleep(1)

pi.i2c_close(spi)

print("finished.")
