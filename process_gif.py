''' parse an animated gif for thermal printing '''
from printer import ThermalPrinter
from PIL import Image
import sys

printer = ThermalPrinter(serialport='/dev/ttyAMA0')
gif = Image.open(sys.argv[1])

# separate out panels and process each one
frame = 0
while frame < 10:
    try:
        # get the current frame
        gif.seek(frame)

        # resize image to printer width
        base_width = 384
        height = int(gif.size[1] * (base_width / float(gif.size[0])))
        converted = gif.resize((base_width, height), Image.ANTIALIAS)

        # convert the image to black and white
        converted = converted.convert('1', dither=3)
        data = list(converted.getdata())
        w, h = converted.size

#        import os
#        converted.save(os.getcwd() + '/output/%d.bmp' % frame)

        printer.print_bitmap(data, w, h, True)
        printer.linefeed()
        printer.linefeed()
        printer.linefeed()

        frame += 1
    except EOFError:
        # found end gif
        break
