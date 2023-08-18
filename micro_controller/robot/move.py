import time
from machine import Pin,PWM,I2C
from ssd1306 import SSD1306_I2C # dont know


MIN_DUTY = 650 # 5 percent of 65025 = 3251.25  # ca. 90 degrees differnece
MAX_DUTY = 5000 # 10 percent of 65025 = 6502.5  # for 90 degrees 9000 
RANGE = MAX_DUTY-MIN_DUTY

pwm = PWM(Pin(28))
pwm.freq(50)

# I2C -----------------

WIDTH = 128
HEIGHT = 64

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
speed = 0.0001
modes = ["max_duty","min_duty","start/next"]
current_mode = 0
current_servo = 0

def move():
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
    oled.fill(0)
    oled.text("current mode: ",0,20)
    oled.text(modes[current_mode],0,30)
    oled.text("max_duty: "+str(MAX_DUTY),0,40)
    oled.text("min_duty: "+str(MIN_DUTY),0,50)
    oled.show()
    
    
    if selectB.value():
        current_mode += 1
        if current_mode >= 3:
            current_mode = 0
        time.sleep(0.3)
            
    if lessB.value():
        if current_mode == 0:
            MAX_DUTY -= 20
        elif current_mode == 1:
            MIN_DUTY -= 20
            
    if moreB.value():
        if current_mode == 0:
            MAX_DUTY += 20
        elif current_mode == 1:
            MIN_DUTY += 20
        elif current_mode == 2:
            oled.text("Running...",0,0)
            oled.show()
            RANGE = MAX_DUTY-MIN_DUTY
            move()
    
    





