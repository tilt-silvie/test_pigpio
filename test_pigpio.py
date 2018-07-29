#!/usr/bin/env python

import time
import pigpio

pi = pigpio.pi()

if not pi.connected:
    exit(0)


# spi = pi.spi_open(0, 1000000, 0) # main SPI, CE0
# spi = pi.spi_open(1, 1000000, 0) # main SPI, CE1
spi = pi.spi_open(0, 1000000, 256) # auxiliary SPI, CE0


for i in range(100):
    pi.spi_write(spi, [1, 2, 3, 4, 5])
    print("printed. no." + str(i))
    time.sleep(1)


pi.spi_close(spi)

print("finished.")
