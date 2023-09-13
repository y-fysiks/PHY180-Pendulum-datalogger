import serial
import time

serial_port = 'COM1'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

datanum = 0

dn = open("datanum.txt", "r")

datanum = int(dn.read())
dn.close()


f = open("data" + datanum, "x")

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').split(' ')

        angle = data[0]
        timestamp = data[1]

        # If data received, print it
        if data:
            print("Timestamp: " + timestamp + " Angle: " + angle)

            f.write(timestamp + ", " + angle + "\n")

            # Give the device time to send data again
            time.sleep(0.005)

# To close the serial port gracefully, use Ctrl+C to break the loop
except KeyboardInterrupt:
    print("Closing the serial port and file.")
    ser.close()
    f.close()