import base64
import io
from PIL import Image, ImageEnhance
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark(pic):
    
    #Store image width and height
    w, h = pic.size
    

    # make the image editable
    drawing = ImageDraw.Draw(pic)
    font = ImageFont.truetype("ani.ttf", 68)
    
    #get text width and height
    text = "© Volodya"
    text_w, text_h = drawing.textsize(text, font)
    
    pos = w - text_w, (h - text_h) - 50
    
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    
    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
   
    pic.paste(c_text, pos, c_text)
    return pic

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    filename = 'static/picha_1.png' 
    with open(filename, 'wb') as f:
        f.write(imgdata)