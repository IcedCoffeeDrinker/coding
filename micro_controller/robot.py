import time
from machine import Pin,PWM,I2C
from ssd1306 import SSD1306_I2C # dont know


MIN_DUTY = 650 # 5 percent of 65025 = 3251.25  # ca. 90 degrees differnece
MAX_DUTY = 5000 # 10 percent of 65025 = 6502.5  # for 90 degrees 9000 
RANGE = MAX_DUTY-MIN_DUTY

pwm = PWM(Pin(28))
pwm.freq(50)

# I2C -----------------

i2c = I2C(0,scl=(Pin(17)),sda=Pin(16),freq=200_000) # 0 for for the i2c0 interface
#i2c = I2C(0) this would use the default pins (gp8 and gp9)
# scl for clock
# sda for dataline
# freq for frequency (no pin requried) normal:100 kHz fast/default: 400 kHz

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

oled.fill(0) # clear screen

# buttons ---------------
selectB  = Pin(13, Pin.IN, Pin.PULL_DOWN)
lessB = Pin(14, Pin.IN, Pin.PULL_DOWN)
moreB = Pin(15, Pin.IN, Pin.PULL_DOWN)

# settings
speed = 0.001
modes = ["max_duty","min_duty","start"]
current_mode = 0

def click():
    for i in range(RANGE):
        duty = MAX_DUTY - i
        pwm.duty_u16(duty)
        time.sleep(speed)
    for i in range(RANGE):
        duty = MIN_DUTY + i
        pwm.duty_u16(duty)
        time.sleep(speed)
    print("click")

while True:
    if selectB.value():
        current_mode += 1
        if current_mode >= 4:
            current_mode = 0
    if lessB.value():
        pass
    if moreB.value():
        pass
    




