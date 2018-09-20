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
