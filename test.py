import serial
import time
import struct

port = '/dev/ttyACM3'

ser = serial.Serial(port, 9600)
sendval = [20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in sendval:
    bytecount = ser.write(chr(i).encode("latin1"))
    print(bytecount)
    time.sleep(3.0)
