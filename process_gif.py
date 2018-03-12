''' parse an animated gif for thermal printing '''
# from printer import ThermalPrinter
from PIL import Image
import sys

GRAYSCALE_CHARS = ['  ','░░','▒▒','▓▓']

# printer = ThermalPrinter(serialport='/dev/ttyAMA0')
gif = Image.open(sys.argv[1])

def l_to_char(l):
    bucket = 255 / 3
    return GRAYSCALE_CHARS[int(l / bucket)]

def to_string(chars):
    data = ""
    for idx, c in enumerate(chars):
        if idx % base_width * 2 == 0:
            data += '\n'
        data += c
    return data

# separate out panels and process each one
frame = 0
while frame < 10:
    try:
        # get the current frame
        gif.seek(frame)

        # resize image to printer width
        base_width = 16
        height = int(gif.size[1] * (base_width / float(gif.size[0])))
        converted = gif.resize((base_width, height), Image.ANTIALIAS)

        # convert the image to black and white
        converted = converted.convert('L')
        values = list(converted.getdata())
        chars = list(map(l_to_char, values))

        print(to_string(chars))

        # import os
        # converted.save(os.getcwd() + '/output/%d.bmp' % frame)

        # print each frame
        # printer.print_bitmap(data, w, h, True)
        # printer.linefeed()

        frame += 1
    except EOFError:
        # found end gif
        break
