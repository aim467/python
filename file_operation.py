file_name = (input("请输入文件名:"))  # 从用户获取文件名字
thefile = open(file_name)  # 打开文件
text = thefile.read()  # 读取文件并赋值到变量text上
file_word_count = len(text)  # 计算文件的字数并赋值给File word count
print("字数为:", file_word_count)  # 输出文件字数
thefile.close()  # 操作完成，关闭文件


count = 0
thefile = open(file_name)  # 打开文件
while True:  # 利用while循环计算文件的行数
    lines = thefile.read()  # 检测文件的行数
    if not lines:  # 如果文件没有行数则退出循环
        break
    count += lines.count('\n')  # 计算行数
    print("行数为:", count)  # 输出行数
thefile.close()  # 操作完成，关闭文件
