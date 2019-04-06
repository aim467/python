import os
import json

import jieba
import magic


def count_words_lines(file):
    """
    此函数用于统计文件的: 行数　个数　词语数量
    :param file:
    :return:
    """

    with open(file) as f:
        words = f.read()
        lines = words.count('\n')
        seg_list = jieba.lcut(words, cut_all=False, HMM=True)
        print("文件总共有{}行, 总共有{}个字, 总共有{}个词语".format(lines, len(words),
                                                   len(seg_list)))


def detection_file_type(file):
    """
    此函数用于检测文件类型 通过读取file_type.json文件和
    分离出来的扩展名作对比
    :param file:
    :return:
    """
    file_extension = os.path.splitext(file)[1]
    f = open("file_type.json")
    data = json.loads(f.read())
    for type in data:
        if type["type"] == file_extension:
            return type["description"]


def magic_file(file):
    """
    此函数用于检测文件类型　使用第三方magic函数
    :param file:
    :return:
    """
    file_type = magic.from_file(file)
    return file_type


if __name__ == "__main__":
    print(count_words_lines("master.txt"))
    print(detection_file_type("master.txt"))
    print(magic_file("master.txt"))