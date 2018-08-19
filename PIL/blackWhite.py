from PIL import Image
from PIL import ImageFilter #导入图像滤波器

# img = Image.open('/home/aim/test.jpg')

# white_img = img.filter(ImageFilter.CONTOUR)
# black_img = img.filter(ImageFilter.FIND_EDGES)

# img.show()
# white_img.show()
# black_img.show()import  Image

#先将图片转化为灰度图 
im = Image.open('/home/aim/python/PIL/test.jpg').convert('L')

# 设置阀值
threshold = 128
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#改变每个点的像素值
bim = im.point(table,'1')

bim.save('binary.jpg') 


