#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont

im = Image.open('/home/aim/python/PIL/smile.jpg')

draw = ImageDraw.Draw(im)
str = "一个纯洁的微笑"
# a = str.encode("utf-8")

font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Thin.ttc',26)

draw.text((32,180),str,font = font,fill = (0,0,0))

im.save('haha.jpg')