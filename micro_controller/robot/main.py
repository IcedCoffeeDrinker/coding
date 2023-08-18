import time
from machine import Pin,PWM,I2C
from ssd1306 import SSD1306_I2C # dont know


MIN_DUTY = 650 # 5 percent of 65025 = 3251.25  # ca. 90 degrees differnece
MAX_DUTY = 5000 # 10 percent of 65025 = 6502.5  # for 90 degrees 9000 
RANGE = MAX_DUTY-MIN_DUTY

pwm1 = PWM(Pin(28))
pwm1.freq(50)
pwm2 = PWM(Pin(27))
pwm2.freq(50)
pwm3 = PWM(Pin(26))
pwm3.freq(50)


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
current_servo = 0
servo_duty = [4000,4000,4000]

def move(duty):
    if current_servo == 0:
        pwm1.duty_u16(duty)
    elif current_servo == 1:
        pwm2.duty_u16(duty)
    elif current_servo == 2:
        pwm1.duty_u16(duty)
    else:
        current_servo = 0
    print("click")

while True:
    oled.fill(0)
    oled.text("current servo: ",0,20)
    oled.text(modes[current_servo],0,30)
    oled.text("duty: "+str(servo_duty[current_servo]),0,40)
    oled.show()
    
    
    if selectB.value():
        current_mode += 1
        if current_servo >= 3:
            current_servo = 0
        time.sleep(0.3)
            
    if lessB.value():
        if current_servo == 0:
            MAX_DUTY -= 20
        elif current_servo == 1:
            MIN_DUTY -= 20
            
    if moreB.value():
        if current_servo == 0:
            MAX_DUTY += 20
        elif current_servo == 1:
            MIN_DUTY += 20
        elif current_servo == 2:
            oled.text("Running...",0,0)
            oled.show()
            RANGE = MAX_DUTY-MIN_DUTY
            move()
    
    




