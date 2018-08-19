from PIL import Image,ImageDraw,ImageFont

im = Image.open('/home/aim/timg.jpg')  #创建图片对象

w,h = im.size  #获取图片大小

font = ImageFont.truetype('/usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf',int(h/3))
# 创建字体对象，设置字体大小
ImageDraw.Draw(im).pieslice([(w/3*2,0),(w,h/3)],0,360,fill = "red")
#填充一个红色的圆
ImageDraw.Draw(im).text((w * 0.74, h * 0.01),'1',font=font,fill = "white")
#第一个是未计读数的位置，第二个设置未计读数的数字，第三个选择填充颜色
im.show()
# 展示图片

im.save('qq.jpg')