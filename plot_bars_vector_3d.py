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
    for z in range(5):
        if vm - (z + 1)*pixelscale >= 0:
            display.set_pixel(4, 4 - z, 9)
        else:
            display.set_pixel(4, 4 - z, 0)
    for y in range(5):
        for x in range(2):
            if vm - (y + x*5)*pixelscale >= 0:
                display.set_pixel(x + 3, 4 - y, 9)
            else:
                display.set_pixel(x + 3, 4 - y, 0)
