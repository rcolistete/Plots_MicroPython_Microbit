# Show bar with up to 25 pixels, from bottom (default) or from top of display
# value >= 0, pixelscale is the value of each pixel.
# E. g., value = 13 and pixelscale = 2 will show 6 leds . 
# fromtop = True shows the bar starting from top of the display.
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