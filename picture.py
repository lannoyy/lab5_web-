import base64
import io
from PIL import Image, ImageEnhance
import numpy as np

def make_grey(img): 
    return img.convert('LA')

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    filename = 'static/picha_1.png' 
    with open(filename, 'wb') as f:
        f.write(imgdata)