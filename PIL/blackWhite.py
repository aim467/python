from PIL import Image
from PIL import ImageFilter  #导入图像滤波器

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
bim = im.point(table, '1')

bim.save('binary.jpg')
