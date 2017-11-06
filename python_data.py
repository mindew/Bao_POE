# Python code that communicate with arduino board via python shell
import serial
import time

ser = serial.Serial('/dev/ttyACM1', 9600)

file = open('values.csv')

# loops forever
while 1:
    line = file.readline()
    # read the line

    # if there's no line, break the loop
    if not line:
        break
    ser.write(line)
    time.sleep(3)
    # read a line from the CSV file in every 3 seconds
    # by sending the value to the listening arduino board
