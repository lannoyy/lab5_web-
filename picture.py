import base64
import io
from PIL import Image, ImageEnhance
import numpy as np

def change_contrast(img, contrast_factor):
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor) 
    return img 

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    filename = 'static/picha_1.jpeg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)