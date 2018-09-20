# Show up to 5 vertical bars from left to right using the components of a vector (list or tuple)
# Each vertical bar starts from bottom of display
# Each component of the vector should be >= 0, pixelscale is the value of each pixel with 1 as default value.
# E. g., vector = (1,2,3,4,5) will show 5 verticals bars, with 1, 2, 3, 4 and 5 leds on. 
def plot_bars(vector, pixelscale = 1):
    for i in range(len(vector)):
        for y in range(5):
            if vector[i] - (y + 1)*pixelscale >= 0:
                display.set_pixel(i, 4 - y, 9)
            else:
                display.set_pixel(i, 4 - y, 0)