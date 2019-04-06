def File_read(file_name):

    file_word_count = 0
    file_line_count = 0

    thefile = open(file_name)  # 打开文件
    lines = thefile.read()  # 检测文件的行数
    file_line_count += lines.count('\n')  # 计算行数
    file_word_count += len(lines)
    thefile.close()  # 操作完成，关闭文件

    return file_line_count, file_word_count


if __name__ == '__main__':
    # 从键盘获取文件名字
    file_name = (input("请输入文件名:"))

    file_line_count, file_word_count = File_read(file_name)

    print("字数为:", file_word_count)
    print("行数为:", file_line_count)
