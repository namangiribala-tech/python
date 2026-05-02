import serial
import time

# Update COM port if needed (Windows: COMx, Linux: /dev/ttyUSB0)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Allow time for Arduino to reset

try:
    while True:
        if arduino.in_waiting:
            status = arduino.readline().decode().strip()
            if status == "FULL":
                print("Water tank is FULL. Current is flowing.")
            elif status == "EMPTY":
                print("Water tank is NOT full. Current is OFF.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user.")
    arduino.close()