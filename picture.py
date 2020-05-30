from PIL import Image, ImageEnhance

def get_image(img):
    return Image.open(img)

def change_contrast(img, contrast_factor):
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor)
    return img 