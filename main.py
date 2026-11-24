from machine import Pin, I2C, RTC
from time import sleep
import dht
from pico_i2c_lcd import I2cLcd

# -----------------------------
# LCD & DHT11 Initialization
# -----------------------------
I2C_ADDR = 0x27     # Change if needed using i2c.scan()
I2C_SDA = 0
I2C_SCL = 1
i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
sensor = dht.DHT11(Pin(15))  # DHT11 data pin GP15

rtc = RTC()
rtc.datetime((2025, 10, 27, 0, 10, 30, 0, 0))  # Set initial time (optional)

lcd.clear()
lcd.putstr("Smart Env Monitor")
sleep(2)
lcd.clear()

# -----------------------------
# Main Loop
# -----------------------------
while True:
    try:
        # Read sensor
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Read current time
        (_, _, _, _, hour, minute, second, _) = rtc.datetime()

        # Display on LCD
        lcd.clear()
        lcd.putstr("Time:%02d:%02d:%02d" % (hour, minute, second))
        lcd.putstr("\nT:%02dC H:%02d%%" % (temp, hum))

        # Print same output in shell
        print("Time: %02d:%02d:%02d" % (hour, minute, second))
        print("T: %02dC  H: %02d%%" % (temp, hum))
        print()

        sleep(2)

    except Exception as e:
        print("Error:", e)
        lcd.clear()
        lcd.putstr("Sensor Error!")
        sleep(2)
