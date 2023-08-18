from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # dont know
import framebuf # to load images
import buffer
from math import floor
WIDTH = 128
HEIGHT = 64

i2c = I2C(0,scl=(Pin(17)),sda=Pin(16),freq=200_000) # 0 for for the i2c0 interface
#i2c = I2C(0) this would use the default pins (gp8 and gp9)
# scl for clock
# sda for dataline
# freq for frequency (no pin requried) normal:100 kHz fast/default: 400 kHz

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

oled.fill(0) # clear screen
#oled.text("hello world",0,0) # 0,0 is top left

array = bytearray(buffer.array)
fb = framebuf.FrameBuffer(array,64,64,framebuf.MONO_HLSB) # save to frame buffer memory
oled.blit(fb,32,0) # to show image and position it

oled.show()