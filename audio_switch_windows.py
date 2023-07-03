import serial

# Create a Serial object
ser = serial.Serial('COM3', 9600)

while True:
    if ser.inWaiting() > 0:  # if data is available to read
        data = ser.readline().decode('utf-8').strip()  # read a line, decode to string and strip newline
        print(data)
