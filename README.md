# 🌦️ Smart Environment Monitor using Raspberry Pi Pico

A simple embedded systems project built using the **Raspberry Pi Pico** and **MicroPython** to monitor environmental conditions in real time. The system measures **temperature** and **humidity** using a DHT11 sensor, displays the readings along with the current time on a 16x2 I2C LCD, and prints the data to the MicroPython shell.

---

## 📌 Features

- 🌡️ Real-time temperature monitoring
- 💧 Real-time humidity monitoring
- 🕒 Displays current time using Raspberry Pi Pico RTC
- 📟 Live output on a 16x2 I2C LCD
- 💻 Serial output in the MicroPython shell
- ⚠️ Basic error handling for sensor failures

---

## 🛠️ Hardware Used

- Raspberry Pi Pico
- DHT11 Temperature & Humidity Sensor
- 16x2 I2C LCD Display
- Breadboard
- Jumper Wires
- USB Cable

---

## 💻 Software Used

- MicroPython
- Thonny IDE
- Raspberry Pi Pico SDK (MicroPython)

---

## 📂 Project Structure

```
weatherstation/
├── main.py      # Main application (sensor reading, LCD output, error handling)
└── README.md
```

`main.py` also needs two LCD driver files on the Pico, `lcd_api.py` and `pico_i2c_lcd.py`. These are the widely used open-source MicroPython I2C LCD driver files and are not copied into this repo. Upload them to the Pico alongside `main.py` using Thonny.

---

## 🔌 Hardware Connections

### DHT11

| DHT11 Pin | Raspberry Pi Pico |
|------------|-------------------|
| VCC | 3.3V |
| GND | GND |
| DATA | GP15 |

### I2C LCD

| LCD Pin | Raspberry Pi Pico |
|----------|-------------------|
| VCC | 5V or VBUS |
| GND | GND |
| SDA | GP0 |
| SCL | GP1 |

> **Note:** The I2C address is set to **0x27**. If your LCD uses a different address, update the value of `I2C_ADDR` in `main.py`.

---

## ▶️ How It Works

1. Initializes the LCD display.
2. Initializes the DHT11 sensor.
3. Sets up the Raspberry Pi Pico Real-Time Clock (RTC).
4. Reads temperature and humidity every 2 seconds.
5. Displays:
   - Current Time
   - Temperature
   - Humidity
6. Prints the same information to the MicroPython shell.
7. Displays an error message if the sensor fails to respond.

---

## 📷 Sample Output

```
Time: 10:30:04
T: 29C  H: 67%
```

LCD Display

```
Time:10:30:04
T:29C H:67%
```

---

## 🚀 Future Improvements

- Add Wi-Fi connectivity using ESP8266/ESP32
- Upload data to Firebase
- Store sensor readings in the cloud
- Display historical graphs on a web dashboard
- Add weather prediction using collected data
- Send alerts when temperature exceeds a threshold

---

## 📚 Skills Demonstrated

- Embedded Systems
- MicroPython Programming
- Raspberry Pi Pico
- Sensor Interfacing
- I2C Communication
- Real-Time Clock (RTC)
- Error Handling
- Hardware Integration

---

## 👨‍💻 Author

**Carain**

Biomedical Engineering Student | Aspiring Software Engineer
