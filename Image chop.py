# https://note.nkmk.me/en/python-pillow-image-crop-trimming/

from PIL import Image

im = Image.open('data/src/astronaut_rect.bmp')


im_crop = im.crop((60, 20, 400, 200))
im_crop.save('data/dst/astronaut_pillow_crop.jpg', quality=95)