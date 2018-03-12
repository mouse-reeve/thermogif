''' parse an animated gif for thermal printing '''
import os
from PIL import Image

gif = Image.open('cat.gif')

# separate out panels and process each one
frame = 0
while frame < 10:
    try:
        gif.seek(frame)
        # convert the image to 4 shades of gray
        converted = gif.convert('LA').convert('RGB')

        # save each frame
        converted.save('%s/output/%d.bmp' % (os.getcwd(), frame))
        frame += 1
    except EOFError:
        # found end gif
        break
