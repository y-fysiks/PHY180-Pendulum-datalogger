import serial
import time

serial_port = 'COM7'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate, timeout=1)

datanum = 0

dn = open("data/datanum.txt", "r")

datanum = dn.read()
dn.close()

dn = open("data/datanum.txt", "w")
dn.write(str(int(datanum) + 1))


f = open("data/data.csv" + datanum, "x")

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').split(' ')

        # If data received, print it
        if len(data) == 2:
            angle = str(float(data[0]) / 1200.0)
            timestamp = data[1]
        
            print("Timestamp: " + timestamp + " Angle: " + angle)

            f.write(timestamp + ", " + angle + "\n")

            # Give the device time to send data again
            time.sleep(0.001)

# To close the serial port gracefully, use Ctrl+C to break the loop
except KeyboardInterrupt:
    print("Closing the serial port and file.")
    ser.close()
    f.close()