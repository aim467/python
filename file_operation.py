
def file(file_name):

     # 从用户获取文件名字
    thefile = open(file_name)  # 打开文件
    lines = thefile.read()  # 检测文件的行数
    file_line_count += lines.count('\n')  # 计算行数
    file_word_count += len(lines)
     # 输出行数
    thefile.close()  # 操作完成，关闭文件

if __name__ == '__main__':
    file_name = (input("请输入文件名:"))
    file_word_count = 0
    file_line_count = 0
    print("字数为:", file_word_count)
    print("行数为:", file_line_count) 