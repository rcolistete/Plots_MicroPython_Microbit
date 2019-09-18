# Plots_MicroPython_Microbit
Plot functions in MicroPython for BBC Micro:bit using the display of 5x5 LEDs.

## Plot Bars v0.1
#### Documentation :  
Show up to 5 vertical bars from left to right using the components of a vector (list or tuple).  
Each vertical bar starts from bottom of display.  
Each component of the vector should be >= 0, pixelscale is the value of each pixel with 1 as default value.  
E. g., vector = (1,2,3,4,5) will show 5 verticals bars, with 1, 2, 3, 4 and 5 leds on.
#### Source code :
    def plot_bars(vector, pixelscale = 1):
        for i in range(len(vector)):
            for y in range(5):
                if vector[i] - (y + 1)*pixelscale >= 0:
                    display.set_pixel(i, 4 - y, 9)
                else:
                    display.set_pixel(i, 4 - y, 0)
#### Example :
    from microbit import *

    def plot_bars(vector, pixelscale = 1):
        for i in range(len(vector)):
            for y in range(5):
                if vector[i] - (y + 1)*pixelscale >= 0:
                    display.set_pixel(i, 4 - y, 9)
                else:
                    display.set_pixel(i, 4 - y, 0)

    while True:
        ax, ay, az = accelerometer.get_values()
        print(ax, ay, az)
        plot_bars((abs(ax), abs(ay), abs(az), 0, (ax*ax + ay*ay + az*az)**0.5), 200)
        sleep(100)
        
## Plot Bar Pixels v0.1
#### Documentation :
Show bar with up to 25 pixels, from bottom (default) or from top of display.  
value >= 0, pixelscale is the value of each pixel.  
E. g., value = 13 and pixelscale = 2 will show 6 leds.   
fromtop = True shows the bar starting from top of the display.
#### Source code :
    def plot_bar_pixels(value, pixelscale, fromtop = False):
        for y in range(5):
            for x in range(5):
                if fromtop:
                    yl = y
                else:
                    yl = 4-y
                diff = value - ((x + 1) + y*5)*pixelscale
                if diff >= 0:
                    display.set_pixel(x, yl, 9)
                else:
                    display.set_pixel(x, yl, 0)
#### Example :
    from microbit import *

    def plot_bar_pixels(value, pixelscale, fromtop = False):
        for y in range(5):
            for x in range(5):
                if fromtop:
                    yl = y
                else:
                    yl = 4-y
                diff = value - ((x + 1) + y*5)*pixelscale
                if diff >= 0:
                    display.set_pixel(x, yl, 9)
                else:
                    display.set_pixel(x, yl, 0)

    compass.calibrate()
    while True:
        BuT = int(compass.get_field_strength()/1000)
        print(BuT)
        plot_bar_pixels(BuT, 4, fromtop=True)
        sleep(100)
        
## Plot Bars Vector 3D v0.1
#### Documentation :  
Show 3 vertical bars (up to 5 pixels), one for each component of the 3D vector (vx, vy, vz), from bottom of display.  
Show also the norm of the vector in the last 2 vertical bars (up to 10 pixels).  
Each component of the vector should be >= 0, pixelscale is the value of each pixel with 1 as default value.  
E. g., (vx, vy, vz) = (1,2,4) will show 3 verticals bars with 1, 2 and 3 leds on, as well the norm as 4th vertical bar 4 leds on.  
#### Source code :
    def plot_bars_vector_3D(vx, vy, vz, pixelscale = 1):
    for x in range(5):
        if vx - (x + 1)*pixelscale >= 0:
            display.set_pixel(0, 4 - x, 9)
        else:
            display.set_pixel(0, 4 - x, 0)
    for y in range(5):
        if vy - (y + 1)*pixelscale >= 0:
            display.set_pixel(1, 4 - y, 9)
        else:
            display.set_pixel(1, 4 - y, 0)
    for z in range(5):
        if vz - (z + 1)*pixelscale >= 0:
            display.set_pixel(2, 4 - z, 9)
        else:
            display.set_pixel(2, 4 - z, 0)
    vm = (vx*vx + vy*vy + vz*vz)**0.5
    for y in range(5):
        for x in range(2):
            if vm - (y + x*5)*pixelscale >= 0:
                display.set_pixel(x + 3, 4 - y, 9)
            else:
                display.set_pixel(x + 3, 4 - y, 0)
#### Example :
    from microbit import *

    def plot_bars_vector_3D(vx, vy, vz, pixelscale = 1):
        for x in range(5):
            if vx - (x + 1)*pixelscale >= 0:
                display.set_pixel(0, 4 - x, 9)
            else:
                display.set_pixel(0, 4 - x, 0)
        for y in range(5):
            if vy - (y + 1)*pixelscale >= 0:
                display.set_pixel(1, 4 - y, 9)
            else:
                display.set_pixel(1, 4 - y, 0)
        for z in range(5):
            if vz - (z + 1)*pixelscale >= 0:
                display.set_pixel(2, 4 - z, 9)
            else:
                display.set_pixel(2, 4 - z, 0)
        vm = (vx*vx + vy*vy + vz*vz)**0.5
        for y in range(5):
            for x in range(2):
                if vm - (y + x*5)*pixelscale >= 0:
                    display.set_pixel(x + 3, 4 - y, 9)
                else:
                    display.set_pixel(x + 3, 4 - y, 0)

    while True:
        ax, ay, az = accelerometer.get_values()
        print(ax, ay, az)
        plot_bars_vector_3D(abs(ax), abs(ay), abs(az), 200)
        sleep(100)
        
## Plot Axis Vector 3D v0.1
#### Documentation :  
Show 3 axis (up to 5 pixels), one for each component of the 3D vector (vx, vy, vz).
x axis is horizontal on bottom of the display, y axis is vertical on left, z axis is the diagonal.  
Each component of the vector should be >= 0, pixelscale is the value of each pixel with 1 as default value.
E. g., (vx, vy, vz) = (2,3,4) will show 2 horizontal pixels, 3 vertical pixels and 4 diagonal pixels.
#### Source code :
    def plot_axis_vector_3D(vx, vy, vz, pixelscale = 1):
        for x in range(5):
            if vx - (x + 1)*pixelscale >= 0:
                display.set_pixel(x, 4, 9)
            else:
                display.set_pixel(x, 4, 0)
        for y in range(5):
            if vy - (y + 1)*pixelscale >= 0:
                display.set_pixel(0, 4 - y, 9)
            else:
                display.set_pixel(0, 4 - y, 0)
        for z in range(5):
            if vz - (z + 1)*pixelscale >= 0:
                display.set_pixel(z, 4 - z, 9)
            else:
                display.set_pixel(z, 4 - z, 0)
#### Example :
    from microbit import *

    def plot_axis_vector_3D(vx, vy, vz, pixelscale = 1):
        for x in range(5):
            if vx - (x + 1)*pixelscale >= 0:
                display.set_pixel(x, 4, 9)
            else:
                display.set_pixel(x, 4, 0)
        for y in range(5):
            if vy - (y + 1)*pixelscale >= 0:
                display.set_pixel(0, 4 - y, 9)
            else:
                display.set_pixel(0, 4 - y, 0)
        for z in range(5):
            if vz - (z + 1)*pixelscale >= 0:
                display.set_pixel(z, 4 - z, 9)
            else:
                display.set_pixel(z, 4 - z, 0)

    while True:
        ax, ay, az = accelerometer.get_values()
        print(ax, ay, az)
        plot_axis_vector_3D(abs(ax), abs(ay), abs(az), 200)
        sleep(100)
