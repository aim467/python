

def file(file_name):
    import jieba

    thefile = open(file_name)  # 打开文件

    text = thefile.read()  # 检测文件的行数

    seg_list = jieba.lcut(text, cut_all=False, HMM=True)
    words = len(seg_list)

    file_word_count = 0
    file_line_count = 0

    file_line_count += lines.count('\n')  # 计算行数
    file_word_count += len(lines)
    print("字数为:", file_word_count)
    print("行数为:", file_line_count) # 输出行数
    print("词数为:",words)
    thefile.close()  # 操作完成，关闭文件

if __name__ == '__main__':
    file_name = input("请输入文件名:")
    file(file_name)
