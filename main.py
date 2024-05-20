import time
import plasma # type: ignore
from plasma import plasma2040 # type: ignore
from pimoroni import RGBLED, Button, Analog # type: ignore

NUM_LEDS = 40
FRONT_LEDS = (0, 20)
BACK_LEDS = (20, 40)
FPS = 60

# Define colours in RGB format (each colour is a tuple of three values: red, green, and blue)
colours = [
    (0, 0, 0),       # Off
    (255, 255, 255), # White
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 0, 255),   # Magenta
    (0, 255, 255)    # Cyan
]

# Control the onboard LED
led = RGBLED(plasma2040.LED_R, plasma2040.LED_G, plasma2040.LED_B)
led.set_rgb(0, 0, 0)

# Set up the buttons
button_rear = Button(plasma2040.BUTTON_A)
button_front = Button(plasma2040.BUTTON_B)
button_onoff = Button(plasma2040.USER_SW)

# Define the led_strip
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, rgbw=True)

# Setup current monitoring
sense = Analog(plasma2040.CURRENT_SENSE, plasma2040.ADC_GAIN, plasma2040.SHUNT_RESISTOR)

# Function to set LED colour 1
def set_colour_1(colour):
    red, green, blue = colour
    for i in range(FRONT_LEDS[0], FRONT_LEDS[1]):
        led_strip.set_rgb(i, red, green, blue)

# Function to set LED colour 2
def set_colour_2(colour):
    red, green, blue = colour
    for i in range(BACK_LEDS[0], BACK_LEDS[1]):
        led_strip.set_rgb(i, red, green, blue)

# Function to change color 1 on button press
def change_colour_1():
    global current_colour_1_index
    current_colour_1_index = (current_colour_1_index + 1) % len(colours)
    set_colour_1(colours[current_colour_1_index])

# Function to change colour 2 on button press
def change_colour_2():
    global current_colour_2_index
    current_colour_2_index = (current_colour_2_index + 1) % len(colours)
    set_colour_2(colours[current_colour_2_index])

# Initialize current color indexes
current_colour_1_index = 0
current_colour_2_index = 0
set_colour_1(colours[current_colour_1_index])
set_colour_2(colours[current_colour_2_index])

led_strip.start(FPS)

# 
while True:
    if button_front.read():
        change_colour_1()
        print(len(colours))
        print(current_colour_1_index)
        print(colours[current_colour_1_index])
        time.sleep(0.1)

    if button_rear.read():
        change_colour_2()
        print(len(colours))
        print(current_colour_2_index)
        print(colours[current_colour_2_index])
        time.sleep(0.1)
