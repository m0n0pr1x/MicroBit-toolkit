from microbit import *

def clear_pixels(intensity):
    [display.set_pixel(i1,i2,intensity) for i1 in range(5) for i2 in range(5)]

clear_pixels(0)
if __name__ == '__main__':
    clear_pixels(0)